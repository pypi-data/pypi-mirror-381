import re
from pathlib import Path
from .context import AnalysisContext


def analyze_language(context: AnalysisContext) -> None:
    """Analyze and detect the script language, updating context metadata."""
    content = context.content
    
    if not content:
        return
    
    # Try explicit language declaration first
    explicit_lang = _extract_explicit_language(content)
    if explicit_lang:
        context.set('lang', explicit_lang)
        return
    
    # Try shebang detection
    shebang_lang = _detect_language_from_shebang(content)
    if shebang_lang:
        context.set('lang', shebang_lang)
        return
    
    # Try file extension detection
    extension_lang = _detect_language_from_extension(context.script_path)
    if extension_lang:
        context.set('lang', extension_lang)
        return





def _extract_explicit_language(content: str) -> str | None:
    lang_patterns = [
        r'#\s*lang:\s*(\w+)',   # Python/Shell style: # lang: py
        r'//\s*lang:\s*(\w+)'   # JavaScript/C style: // lang: js
    ]
    
    for pattern in lang_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            lang = match.group(1).lower()
            return _normalize_language(lang)
    return None


def _detect_language_from_shebang(content: str) -> str | None:
    lines = content.split('\n')
    
    for line in lines:
        line = line.strip()
        if line.startswith('#!') and 'scriptthing-run' not in line:
            return _extract_interpreter_from_shebang(line)
    
    return None


def _extract_interpreter_from_shebang(shebang_line: str) -> str | None:
    interpreter_patterns = {
        r'python[0-9.]*': 'python',
        r'bash': 'shell',
        r'sh': 'shell',
        r'ruby': 'ruby',
        r'perl': 'perl',
        r'php': 'php'
    }
    
    for pattern, language in interpreter_patterns.items():
        if re.search(pattern, shebang_line, re.IGNORECASE):
            return language
    
    return None


def _detect_language_from_extension(script_path: Path) -> str | None:
    extension_map = {
        '.py': 'python',
        '.sh': 'shell',
        '.bash': 'shell',
        '.rb': 'ruby',
        '.pl': 'perl',
        '.php': 'php',
        '.go': 'go',
        '.rs': 'rust',
        '.cpp': 'cpp',
        '.c': 'c',
        '.java': 'java'
    }
    
    ext = script_path.suffix.lower()
    return extension_map.get(ext)


def _normalize_language(lang: str) -> str:
    aliases = {
        'py': 'python',
        'sh': 'shell',
        'rb': 'ruby',
        'pl': 'perl'
    }
    return aliases.get(lang, lang)