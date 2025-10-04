"""
Simplified parallel execution CLI following AWS SDE3 Leandro's recommendations.

Single stream command with optional chunking, using existing scriptthing patterns.
"""

import click
import sys
from typing import Optional
from scriptthing.core.parallel import stream as stream_execute
from scriptthing.utils.pretty import Print


@click.command("stream")
@click.argument("template", type=str)
@click.option("--input", "-i", "input_file", type=click.Path(exists=True), 
              help="Input file (default: stdin)")
@click.option("--output", "-o", "output_file", type=click.Path(), 
              help="Output file (default: stdout)")
@click.option("--chunk", "-c", type=int,
              help="Process in chunks of this size (default: individual items)")
@click.option("--workers", "-w", type=int, 
              help="Number of workers (default: CPU cores)")
@click.option("--separator", "-s", 
              help="Custom separator for text lines (default: whitespace)")
@click.option("--jinja", "-j", is_flag=True, 
              help="Use Jinja2 templating (default: f-string)")
@click.option("--quiet", "-q", is_flag=True, 
              help="Suppress execution info")
@click.option("--print", "-p", is_flag=True, 
              help="Print commands instead of running them")
def stream(
    template: str,
    input_file: Optional[str],
    output_file: Optional[str],
    chunk: Optional[int],
    workers: Optional[int],
    separator: Optional[str],
    jinja: bool,
    quiet: bool,
    print: bool
) -> None:
    """Stream parallel execution with templated commands.
    
    Automatically detects input format and processes data in parallel.
    Templates can be shell commands or script arguments.
    
    MODES:
      • Individual items (default): Process each item separately
      • Chunked (--chunk N): Process data in chunks of N items
    
    AUTO-DETECTION (following scriptthing stdin patterns):
      • JSON arrays: [{"id":1}] → individual objects or chunks
      • JSONL: {"id":1}\\n{"id":2} → individual records or chunks
      • CSV: id,name\\n1,Alice → individual rows or chunks
      • Text: word1 word2\\nword3 word4 → individual lines or chunks
    
    TEMPLATING:
      • Shell commands (auto-detected): echo {_1} | sort
      • Script arguments (auto-detected): my-script --id {_1}
      • F-string (default): {field} or {_1}
      • Jinja2 (--jinja): {{ field }} or {{ _1|upper }}
    
    POSITIONAL VARIABLES:
      • JSON: _1, _2, _3... = values in key order
      • CSV: _1, _2, _3... = column values  
      • Text: _1, _2, _3... = words in line (split by --separator)
      • JSONL: _1, _2, _3... = field values
    
    EXAMPLES:
      # Shell commands (auto-detected from pipes/redirects)
      echo "hello world\\ntest data" | scriptthing stream 'echo "{_1} -> {_2}"'
      
      # Script arguments (auto-detected from script name)
      echo "word1 word2" | scriptthing stream 'my-script --arg {_1}'
      
      # Complex shell pipelines
      cat urls.txt | scriptthing stream 'curl {_1} | jq .name'
      
             # Chunked processing for large datasets
       scriptthing stream 'process-chunk' -c 100 -i large-file.txt
       
       # Custom separators
       scriptthing stream 'echo {_1}:{_2}' -s ':' -i data.txt
       
       # CSV field mapping
       scriptthing stream 'api-call --user {name} --id {id}' -i users.csv
       
       # Jinja2 templating
       scriptthing stream '{{ _1|upper }}' -j -i data.txt
    """
    try:
        # Read input using scriptthing stdin pattern
        if input_file:
            with open(input_file, 'r') as f:
                input_data = f.read()
        else:
            input_data = sys.stdin.read()
        
        if not input_data.strip():
            Print.error_stderr("No input data provided")
            return
        
        # Validate Jinja2 template if specified
        if jinja and not ('{{' in template and '}}' in template):
            Print.error_stderr("Jinja2 templates must use {{ field }} syntax")
            return
        
        # Execute in parallel with streaming output
        output_file_handle = None
        if output_file:
            output_file_handle = open(output_file, 'w')
        
        total_items = 0
        successful_items = 0
        errors = []
        stderr_messages = []
        
        try:
            # Stream results as they complete
            for result in stream_execute(
                template=template,
                input_data=input_data,
                chunk_size=chunk,
                workers=workers,
                separator=separator,
                _print=print
            ):
                total_items += 1
                
                if result.startswith("ERROR:"):
                    errors.append(result)
                    # Display errors to stderr stream
                    Print.error_stderr(result)
                elif result.startswith("STDERR:"):
                    stderr_messages.append(result)
                    # Display stderr to stderr stream (not stdout or output file)
                    Print.warn_stderr(result)
                else:
                    successful_items += 1
                    # Stream output immediately
                    if output_file_handle:
                        output_file_handle.write(result + '\n')
                        output_file_handle.flush()  # Ensure immediate write
                    else:
                        Print.plain(result)
        
        finally:
            if output_file_handle:
                output_file_handle.close()
                Print.confirm(f"Results streamed to {output_file}")
        
        # Show execution info unless quiet
        if not quiet:
            mode = f"Chunked ({chunk})" if chunk else "Individual"
            template_engine = "jinja2" if jinja else "f-string"
            
            # Build status message
            status_parts = [f"{successful_items}/{total_items} successful"]
            if stderr_messages:
                status_parts.append(f"{len(stderr_messages)} with stderr")
            if errors:
                status_parts.append(f"{len(errors)} errors")
            
            status_msg = f"Stream {mode}: {', '.join(status_parts)} ({template_engine})"
            
            if errors:
                Print.error_stderr(status_msg)
            elif stderr_messages:
                Print.warn_stderr(status_msg)
            else:
                Print.confirm(status_msg)
        
        # Exit with error if any items failed
        if errors:
            click.get_current_context().exit(1)
            
    except Exception as e:
        Print.error_stderr(f"Stream error: {e}")
        click.get_current_context().exit(1)


def register_parallel_commands(cli_group: click.Group) -> None:
    """Register the unified stream command."""
    cli_group.add_command(stream)
