#!/usr/bin/env scriptthing-run
# lang: py

# MCP Metadata (uncomment and modify for MCP support):
# MCP_NAME: example_tool
# MCP_DESCRIPTION: Example Python script tool
# MCP_PARAM: input_text:string:Text to process:true

import sys
from dataclasses import dataclass
from scriptthing import stdin, argsclass, Required, Flag, Option


# Define CLI arguments using enhanced argsclass
@dataclass
class Args:
    """Script arguments with validation and help."""
    
    # Required input
    input_text: Required(str)
    
    # Optional parameters with validation
    output_format: Option(str, choices=["json", "yaml", "text"], help="Output format") = "text"
    max_length: Option(int, min_value=1, max_value=1000, help="Maximum output length") = 100
    
    # Flags
    verbose: Flag() = False
    uppercase: Flag() = False


def main():
    """Main script function."""
    # Parse command line arguments
    args = argsclass(Args)
    
    # Process input
    text = args.input_text
    
    if args.uppercase:
        text = text.upper()
    
    # Truncate if needed
    if len(text) > args.max_length:
        text = text[:args.max_length] + "..."
    
    # Output in requested format
    if args.output_format == "json":
        import json
        result = {"text": text, "length": len(text)}
        print(json.dumps(result, indent=2))
    elif args.output_format == "yaml":
        print(f"text: {text}")
        print(f"length: {len(text)}")
    else:
        print(text)
    
    if args.verbose:
        print(f"Processed {len(args.input_text)} characters", file=sys.stderr)


if __name__ == "__main__":
    main()
