# Utilities for defining argparse CLI interfaces quickly in scripts
import argparse
import sys
from dataclasses import MISSING, dataclass, fields
from typing import Annotated, TypeVar, Any, List, Optional, Union, Callable, get_origin, get_args, Generic
from typing import Type
from pathlib import Path
from enum import Enum


ArgType = Union[str, bool, int, float]

T = TypeVar('T')

def _transform_name(name: str):
    return f"--{name.replace('_', '-')}"

def _positional_name(name: str):
    return name

# Enhanced annotation system
class ArgumentConfig:
    """Configuration for command line arguments."""
    def __init__(
        self,
        *,
        required: bool = False,
        default: Any = MISSING,
        help: str = "",
        choices: Optional[List[str]] = None,
        min_value: Optional[Union[int, float]] = None,
        max_value: Optional[Union[int, float]] = None,
        validator: Optional[Callable[[Any], bool]] = None,
        metavar: Optional[str] = None,
        dest: Optional[str] = None,
        action: Optional[str] = None,
        nargs: Optional[Union[str, int]] = None,
        const: Any = None,
        positional: bool = False,
        hidden: bool = False
    ):
        self.required = required
        self.default = default
        self.help = help
        self.choices = choices
        self.min_value = min_value
        self.max_value = max_value
        self.validator = validator
        self.metavar = metavar
        self.dest = dest
        self.action = action
        self.nargs = nargs
        self.const = const
        self.positional = positional
        self.hidden = hidden

# Generic type factory base class
class _ArgumentType(Generic[T]):
    """Base class for argument types that support __getitem__ syntax."""
    
    def __init__(self, config: ArgumentConfig):
        self._config = config
    
    def __getitem__(self, type_hint: Type[T]) -> Type[T]:
        """Support for TypeName[ActualType] syntax."""
        return Annotated[type_hint, self._config]
    
    def __call__(self, type_hint: Type[T] = str) -> Type[T]:
        """Backward compatibility support for TypeName(ActualType) syntax."""
        return Annotated[type_hint, self._config]

# Type factory instances using proper generic syntax
class _RequiredType(_ArgumentType[T]):
    """Create a required argument annotation."""
    def __init__(self):
        super().__init__(ArgumentConfig(required=True))

class _PositionalType(_ArgumentType[T]):
    """Create a positional argument annotation."""
    def __init__(self):
        super().__init__(ArgumentConfig(positional=True))

class _FlagType(_ArgumentType[bool]):
    """Create a boolean flag annotation."""
    def __init__(self):
        super().__init__(ArgumentConfig(action="store_true"))
    
    def __getitem__(self, type_hint: Type[bool] = bool) -> Type[bool]:
        """Flags are always bool type."""
        return Annotated[bool, self._config]
    
    def __call__(self) -> Type[bool]:
        """Backward compatibility - flags don't take type parameters."""
        return Annotated[bool, self._config]

class _CounterType(_ArgumentType[int]):
    """Create a counter annotation."""
    def __init__(self):
        super().__init__(ArgumentConfig(action="count"))
    
    def __getitem__(self, type_hint: Type[int] = int) -> Type[int]:
        """Counters are always int type."""
        return Annotated[int, self._config]
    
    def __call__(self) -> Type[int]:
        """Backward compatibility - counters don't take type parameters."""
        return Annotated[int, self._config]

class _HiddenType(_ArgumentType[T]):
    """Create a hidden argument annotation."""
    def __init__(self):
        super().__init__(ArgumentConfig(hidden=True))

# Create instances of the type factories
Required = _RequiredType()
Positional = _PositionalType()
Flag = _FlagType()
Counter = _CounterType()
Hidden = _HiddenType()

# Option type factory with parameters
class _OptionType(_ArgumentType[T]):
    """Create an option argument with validation."""
    
    def __init__(self):
        # Initialize with a default config for the base class
        super().__init__(ArgumentConfig())
    
    def __getitem__(self, type_hint: Type[T]) -> Type[T]:
        """Support for Option[ActualType] syntax - returns basic option."""
        return Annotated[type_hint, ArgumentConfig()]
    
    def __call__(
        self,
        type_hint: Type[T] = str,
        *,
        required: bool = False,
        default: Any = MISSING,
        help: str = "",
        choices: Optional[List[str]] = None,
        min_value: Optional[Union[int, float]] = None,
        max_value: Optional[Union[int, float]] = None,
        validator: Optional[Callable[[Any], bool]] = None,
        metavar: Optional[str] = None,
        hidden: bool = False
    ) -> Type[T]:
        """Create an option with specific configuration."""
        config = ArgumentConfig(
            required=required,
            default=default,
            help=help,
            choices=choices,
            min_value=min_value,
            max_value=max_value,
            validator=validator,
            metavar=metavar,
            hidden=hidden
        )
        return Annotated[type_hint, config]

Option = _OptionType()

class _ArgumentTypeFactory(_ArgumentType[T]):
    """Create a positional argument with validation."""
    
    def __init__(self):
        # Initialize with a default config for the base class
        super().__init__(ArgumentConfig(positional=True))
    
    def __getitem__(self, type_hint: Type[T]) -> Type[T]:
        """Support for Argument[ActualType] syntax - returns basic positional argument."""
        return Annotated[type_hint, ArgumentConfig(positional=True)]
    
    def __call__(
        self,
        type_hint: Type[T] = str,
        *,
        help: str = "",
        choices: Optional[List[str]] = None,
        validator: Optional[Callable[[Any], bool]] = None,
        metavar: Optional[str] = None,
        nargs: Optional[Union[str, int]] = None
    ) -> Type[T]:
        """Create a positional argument with specific configuration."""
        config = ArgumentConfig(
            positional=True,
            help=help,
            choices=choices,
            validator=validator,
            metavar=metavar,
            nargs=nargs
        )
        return Annotated[type_hint, config]

Argument = _ArgumentTypeFactory()


class ValidationError(Exception):
    """Raised when argument validation fails."""
    pass

def _validate_value(value: Any, config: ArgumentConfig, field_name: str) -> Any:
    """Validate a parsed value against its configuration."""
    if config.choices and value not in config.choices:
        raise ValidationError(f"Invalid choice for {field_name}: {value}. Must be one of {config.choices}")
    
    if config.min_value is not None and isinstance(value, (int, float)):
        if value < config.min_value:
            raise ValidationError(f"Value for {field_name} must be >= {config.min_value}")
    
    if config.max_value is not None and isinstance(value, (int, float)):
        if value > config.max_value:
            raise ValidationError(f"Value for {field_name} must be <= {config.max_value}")
    
    if config.validator and not config.validator(value):
        raise ValidationError(f"Validation failed for {field_name}: {value}")
    
    return value

def _get_type_and_config(field_type: Type) -> tuple[Type, ArgumentConfig]:
    """Extract the actual type and ArgumentConfig from an annotated type."""
    # Check if this is an Annotated type
    origin = get_origin(field_type)
    if origin is not None:
        # This is a generic type like Annotated[str, ...]
        args = get_args(field_type)
        if args:
            actual_type = args[0]  # The first argument is the actual type
            
            # Look for ArgumentConfig in the metadata
            config = None
            if hasattr(field_type, "__metadata__"):
                for metadata in field_type.__metadata__:
                    if isinstance(metadata, ArgumentConfig):
                        config = metadata
                        break
                    # Legacy support for old format
                    elif callable(metadata) and hasattr(metadata, '__name__'):
                        # Old transform function
                        if len(field_type.__metadata__) > 1:
                            legacy_kwargs = field_type.__metadata__[1]
                            if isinstance(legacy_kwargs, dict):
                                config = ArgumentConfig(**legacy_kwargs)
                            else:
                                config = ArgumentConfig()
                        else:
                            config = ArgumentConfig()
                        break
            
            if config is None:
                config = ArgumentConfig()
            
            return actual_type, config
        else:
            return field_type, ArgumentConfig()
    else:
        # Not a generic type, check for old-style __metadata__
        if hasattr(field_type, "__metadata__"):
            # Handle legacy annotations
            metadata = field_type.__metadata__
            if len(metadata) >= 2 and isinstance(metadata[1], dict):
                config = ArgumentConfig(**metadata[1])
                # Try to get the actual type from __origin__ or __args__
                if hasattr(field_type, "__origin__"):
                    actual_type = field_type.__origin__
                elif hasattr(field_type, "__args__") and field_type.__args__:
                    actual_type = field_type.__args__[0]
                else:
                    actual_type = str
                return actual_type, config
        
        return field_type, ArgumentConfig()

def _setup_argument(parser: argparse.ArgumentParser, field, actual_type: Type, config: ArgumentConfig):
    """Set up a single argument in the parser."""
    kwargs = {}
    
    # Handle basic properties
    if config.help:
        kwargs["help"] = config.help
    if config.metavar:
        kwargs["metavar"] = config.metavar
    if config.dest:
        kwargs["dest"] = config.dest
    if config.nargs:
        kwargs["nargs"] = config.nargs
    if config.const is not None:
        kwargs["const"] = config.const
    
    # Handle choices
    if config.choices:
        kwargs["choices"] = config.choices
    
    # Handle defaults
    if config.default is not MISSING:
        kwargs["default"] = config.default
    elif field.default is not MISSING:
        kwargs["default"] = field.default
    elif field.default_factory is not MISSING:
        kwargs["default"] = field.default_factory()
    elif not config.required and not config.positional:
        kwargs["default"] = None
    
    # Handle actions
    if config.action:
        kwargs["action"] = config.action
        if config.action in ("store_true", "store_false"):
            # Don't set type for boolean actions
            pass
        elif config.action == "count":
            if "default" not in kwargs:
                kwargs["default"] = 0
        else:
            # Only set type if it's a valid type for argparse
            if actual_type not in (bool, type(None)):
                kwargs["type"] = actual_type
    else:
        # Set type if not using special actions
        if actual_type == bool:
            kwargs["action"] = "store_true"
        elif actual_type not in (type(None),):
            # Only set type if it's a real type
            kwargs["type"] = actual_type
    
    # Handle required flag
    if config.required and not config.positional:
        kwargs["required"] = True
    
    # Determine argument name(s)
    if config.positional:
        arg_names = [field.name]
    else:
        arg_names = [f"--{field.name.replace('_', '-')}"]
        # Add short option if available and not already used
        short_name = f"-{field.name[0]}"
        if not hasattr(parser, '_short_names'):
            parser._short_names = set()
        
        if short_name not in parser._short_names and short_name not in ['-h']:  # Avoid conflict with help
            parser._short_names.add(short_name)
            arg_names.insert(0, short_name)
    
    # Add the argument
    parser.add_argument(*arg_names, **kwargs)

def args(*args: str, **kwargs: ArgType):
    """Simple argument parsing for basic use cases."""
    parser = argparse.ArgumentParser()
    for arg in args:
        parser.add_argument(arg)
    for k, v in kwargs.items():
        name = f"--{k.replace('_', '-')}"
        parser.add_argument(name, default=v)
    return parser.parse_args()

def from_class(cls: Type[T]) -> T:
    """Enhanced argument parsing from a dataclass with validation."""
    # Get class name for parser description
    class_name = getattr(cls, '__name__', 'CLI')
    description = getattr(cls, '__doc__', None)
    
    parser = argparse.ArgumentParser(
        prog=class_name,
        description=description,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Ensure it's a dataclass
    if not hasattr(cls, "__dataclass_fields__"):
        cls = dataclass(cls)
    
    # Track positional arguments separately to maintain order
    positional_fields = []
    option_fields = []
    
    for field in fields(cls):
        actual_type, config = _get_type_and_config(field.type)
        
        if config.hidden:
            continue
            
        if config.positional:
            positional_fields.append((field, actual_type, config))
        else:
            option_fields.append((field, actual_type, config))
    
    # Add positional arguments first
    for field, actual_type, config in positional_fields:
        _setup_argument(parser, field, actual_type, config)
    
    # Add optional arguments
    for field, actual_type, config in option_fields:
        _setup_argument(parser, field, actual_type, config)
    
    # Parse arguments
    try:
        parsed_args = parser.parse_args()
        parsed_dict = vars(parsed_args)
        
        # Validate parsed values
        for field in fields(cls):
            actual_type, config = _get_type_and_config(field.type)
            if config.hidden:
                continue
                
            field_name = field.name
            if field_name in parsed_dict:
                value = parsed_dict[field_name]
                if value is not None:  # Skip validation for None values
                    try:
                        validated_value = _validate_value(value, config, field_name)
                        parsed_dict[field_name] = validated_value
                    except ValidationError as e:
                        parser.error(str(e))
        
        return cls(**parsed_dict)
        
    except SystemExit:
        # Re-raise SystemExit for help/error handling
        raise
    except Exception as e:
        parser.error(f"Error creating {class_name}: {e}")

def cli_class(cls: type):
    """Decorator to make a class into a CLI interface."""
    return from_class(dataclass(cls))

# Utility functions for common patterns
def file_path_validator(path: str) -> bool:
    """Validator for file paths."""
    return Path(path).exists()

def directory_path_validator(path: str) -> bool:
    """Validator for directory paths."""
    return Path(path).is_dir()

def positive_int_validator(value: int) -> bool:
    """Validator for positive integers."""
    return value > 0

def non_negative_int_validator(value: int) -> bool:
    """Validator for non-negative integers."""
    return value >= 0

# Common argument configurations - factory classes for proper type hints
class _FilePathArgType(_ArgumentType[str]):
    """File path argument with existence validation."""
    
    def __init__(self):
        # Initialize with a default config for the base class
        super().__init__(ArgumentConfig(
            required=True,
            help="Path to file",
            validator=file_path_validator,
            metavar="FILE"
        ))
    
    def __getitem__(self, type_hint: Type[str] = str) -> Type[str]:
        """FilePathArg is always str type."""
        return Annotated[str, ArgumentConfig(
            required=True,
            help="Path to file",
            validator=file_path_validator,
            metavar="FILE"
        )]
    
    def __call__(self, *, required: bool = True, help: str = "Path to file") -> Type[str]:
        """Create a file path argument with validation."""
        return Annotated[str, ArgumentConfig(
            required=required,
            help=help,
            validator=file_path_validator,
            metavar="FILE"
        )]

class _DirPathArgType(_ArgumentType[str]):
    """Directory path argument with existence validation."""
    
    def __init__(self):
        # Initialize with a default config for the base class
        super().__init__(ArgumentConfig(
            required=True,
            help="Path to directory",
            validator=directory_path_validator,
            metavar="DIR"
        ))
    
    def __getitem__(self, type_hint: Type[str] = str) -> Type[str]:
        """DirPathArg is always str type."""
        return Annotated[str, ArgumentConfig(
            required=True,
            help="Path to directory",
            validator=directory_path_validator,
            metavar="DIR"
        )]
    
    def __call__(self, *, required: bool = True, help: str = "Path to directory") -> Type[str]:
        """Create a directory path argument with validation."""
        return Annotated[str, ArgumentConfig(
            required=required,
            help=help,
            validator=directory_path_validator,
            metavar="DIR"
        )]

class _PortArgType(_ArgumentType[int]):
    """Port number argument with range validation."""
    
    def __init__(self):
        # Initialize with a default config for the base class
        super().__init__(ArgumentConfig(
            default=8080,
            help="Port number",
            min_value=1,
            max_value=65535,
            metavar="PORT"
        ))
    
    def __getitem__(self, type_hint: Type[int] = int) -> Type[int]:
        """PortArg is always int type."""
        return Annotated[int, ArgumentConfig(
            default=8080,
            help="Port number",
            min_value=1,
            max_value=65535,
            metavar="PORT"
        )]
    
    def __call__(self, *, default: int = 8080, help: str = "Port number") -> Type[int]:
        """Create a port number argument with validation."""
        return Annotated[int, ArgumentConfig(
            default=default,
            help=help,
            min_value=1,
            max_value=65535,
            metavar="PORT"
        )]

class _VerbosityArgType(_ArgumentType[int]):
    """Verbosity level argument (counts -v flags)."""
    
    def __init__(self):
        # Initialize with a default config for the base class
        super().__init__(ArgumentConfig(
            action="count",
            default=0,
            help="Increase verbosity (use multiple times)"
        ))
    
    def __getitem__(self, type_hint: Type[int] = int) -> Type[int]:
        """VerbosityArg is always int type."""
        return Annotated[int, ArgumentConfig(
            action="count",
            default=0,
            help="Increase verbosity (use multiple times)"
        )]
    
    def __call__(self) -> Type[int]:
        """Create a verbosity argument."""
        return Annotated[int, ArgumentConfig(
            action="count",
            default=0,
            help="Increase verbosity (use multiple times)"
        )]

# Create instances
FilePathArg = _FilePathArgType()
DirPathArg = _DirPathArgType()
PortArg = _PortArgType()
VerbosityArg = _VerbosityArgType()

# Enhanced export for better IDE support
__all__ = [
    'args', 'from_class', 'cli_class', 'argsclass',
    'Required', 'Positional', 'Flag', 'Counter', 'Hidden',
    'Option', 'Argument', 'ArgumentConfig', 'ValidationError',
    'FilePathArg', 'DirPathArg', 'PortArg', 'VerbosityArg',
    'file_path_validator', 'directory_path_validator', 
    'positive_int_validator', 'non_negative_int_validator'
]

# Backward compatibility alias
argsclass = cli_class