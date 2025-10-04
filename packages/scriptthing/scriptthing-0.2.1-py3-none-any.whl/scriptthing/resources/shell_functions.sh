#!/bin/bash

# Shell bindings for scriptthing scripts
# Source this file to get convenient shell functions for calling scriptthing scripts
# Note: This file contains functions that should only be sourced in bash scripts.
# For shell extensions that should be available in all shells, use 'scriptthing new extension <name>'

# Configuration
SCRIPTTHING_BIN_DIR="${SCRIPTTHING_BIN_DIR:-$HOME/.local/scriptthing/bin}"
SCRIPTTHING_TIMEOUT="${SCRIPTTHING_TIMEOUT:-30}"

# Colors for output
if [ -t 1 ]; then
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    YELLOW='\033[1;33m'
    BLUE='\033[0;34m'
    NC='\033[0m'
else
    RED=''
    GREEN=''
    YELLOW=''
    BLUE=''
    NC=''
fi

# Logging functions
st_log_info() {
    printf "${BLUE}[INFO]${NC} %s\n" "$1" >&2
}

st_log_success() {
    printf "${GREEN}[SUCCESS]${NC} %s\n" "$1" >&2
}

st_log_warning() {
    printf "${YELLOW}[WARNING]${NC} %s\n" "$1" >&2
}

st_log_error() {
    printf "${RED}[ERROR]${NC} %s\n" "$1" >&2
}

# Check if scriptthing script exists
st_script_exists() {
    local script_name="$1"
    [ -x "$SCRIPTTHING_BIN_DIR/$script_name" ]
}

# List available scriptthing scripts
st_list_scripts() {
    if [ -d "$SCRIPTTHING_BIN_DIR" ]; then
        find "$SCRIPTTHING_BIN_DIR" -maxdepth 1 -type f -executable -exec basename {} \; | sort
    else
        st_log_error "Scriptthing bin directory not found: $SCRIPTTHING_BIN_DIR"
        return 1
    fi
}

# Execute a scriptthing script with timeout and error handling
st_call() {
    local script_name="$1"
    shift
    
    if ! st_script_exists "$script_name"; then
        st_log_error "Script '$script_name' not found in $SCRIPTTHING_BIN_DIR"
        return 1
    fi
    
    local script_path="$SCRIPTTHING_BIN_DIR/$script_name"
    
    # Execute with timeout if available
    if command -v timeout >/dev/null 2>&1; then
        timeout "$SCRIPTTHING_TIMEOUT" "$script_path" "$@"
    else
        "$script_path" "$@"
    fi
}

# Execute a script and capture output in variables
st_call_capture() {
    local script_name="$1"
    local stdout_var="$2"
    local stderr_var="$3"
    local return_var="$4"
    shift 4
    
    local temp_stdout=$(mktemp)
    local temp_stderr=$(mktemp)
    local exit_code
    
    st_call "$script_name" "$@" >"$temp_stdout" 2>"$temp_stderr"
    exit_code=$?
    
    if [[ -n "$stdout_var" ]]; then
        eval "$stdout_var"='$(cat "$temp_stdout")'
    fi
    
    if [[ -n "$stderr_var" ]]; then
        eval "$stderr_var"='$(cat "$temp_stderr")'
    fi
    
    if [[ -n "$return_var" ]]; then
        eval "$return_var"="$exit_code"
    fi
    
    rm -f "$temp_stdout" "$temp_stderr"
    return $exit_code
}

# Call script with JSON input
st_call_json() {
    local script_name="$1"
    local json_data="$2"
    shift 2
    
    echo "$json_data" | st_call "$script_name" "$@"
}

# Call script and parse JSON output
st_call_parse_json() {
    local script_name="$1"
    local output_var="$2"
    shift 2
    
    local json_output
    if json_output=$(st_call "$script_name" "$@"); then
        if command -v jq >/dev/null 2>&1; then
            eval "$output_var"='$(echo "$json_output" | jq -c .)'
        else
            eval "$output_var"='"$json_output"'
        fi
        return 0
    else
        return 1
    fi
}

# Convenience functions for common scripts

# Analyze disk usage
st_analyze_disk_usage() {
    local directory="${1:-.}"
    local depth="${2:-2}"
    local format="${3:-summary}"
    
    local args="$directory --depth $depth"
    
    case "$format" in
        "summary")
            args="$args --summary"
            ;;
        "json")
            args="$args --pretty"
            ;;
        *)
            st_log_error "Invalid format '$format'. Use 'summary' or 'json'"
            return 1
            ;;
    esac
    
    eval "st_call analyze-disk-usage $args"
}

# Backup files
st_backup_files() {
    local sources=""
    local dest=""
    local compression="gzip"
    local verbose=false
    local exclude=""
    
    # Parse options (simple implementation)
    while [ $# -gt 0 ]; do
        case "$1" in
            --dest|-d)
                dest="$2"
                shift 2
                ;;
            --compress|-c)
                compression="$2"
                shift 2
                ;;
            --verbose|-v)
                verbose=true
                shift
                ;;
            --exclude|-e)
                exclude="$exclude $2"
                shift 2
                ;;
            *)
                sources="$sources $1"
                shift
                ;;
        esac
    done
    
    local args=""
    [ -n "$dest" ] && args="$args --dest $dest"
    [ "$compression" != "gzip" ] && args="$args --compress $compression"
    [ "$verbose" = "true" ] && args="$args --verbose"
    
    for pattern in $exclude; do
        args="$args --exclude $pattern"
    done
    
    args="$args $sources"
    
    eval "st_call backup-files $args"
}

# Convert CSV to JSON
st_csv_to_json() {
    local input_file="$1"
    local format="${2:-array}"
    local pretty="${3:-false}"
    
    local args=""
    
    case "$format" in
        "lines")
            args="$args --lines"
            ;;
        "array")
            # Default, no additional args
            ;;
        *)
            st_log_error "Invalid format '$format'. Use 'array' or 'lines'"
            return 1
            ;;
    esac
    
    [ "$pretty" = "true" ] && args="$args --pretty"
    
    if [ -n "$input_file" ] && [ -f "$input_file" ]; then
        cat "$input_file" | eval "st_call csv-to-json $args"
    else
        eval "st_call csv-to-json $args"
    fi
}

# Query JSON with jq-lite
st_query_json() {
    local query="${1:-.}"
    local input_file="$2"
    local raw="${3:-false}"
    local pretty="${4:-false}"
    
    local args="$query"
    [ "$raw" = "true" ] && args="$args --raw"
    [ "$pretty" = "true" ] && args="$args --pretty"
    
    if [ -n "$input_file" ] && [ -f "$input_file" ]; then
        cat "$input_file" | eval "st_call jq-lite $args"
    else
        eval "st_call jq-lite $args"
    fi
}

# Filter logs
st_filter_logs() {
    local input_file="$1"
    shift
    
    local level=""
    local contains=""
    local count_only=false
    local stats=false
    
    while [ $# -gt 0 ]; do
        case "$1" in
            --level)
                level="$2"
                shift 2
                ;;
            --contains)
                contains="$2"
                shift 2
                ;;
            --count)
                count_only=true
                shift
                ;;
            --stats)
                stats=true
                shift
                ;;
            *)
                st_log_error "Unknown option: $1"
                return 1
                ;;
        esac
    done
    
    local args=""
    [ -n "$level" ] && args="$args --level $level"
    [ -n "$contains" ] && args="$args --contains $contains"
    [ "$count_only" = "true" ] && args="$args --count"
    [ "$stats" = "true" ] && args="$args --stats"
    
    if [ -n "$input_file" ] && [ -f "$input_file" ]; then
        cat "$input_file" | eval "st_call log-filter $args"
    else
        eval "st_call log-filter $args"
    fi
}

# Network scan
st_network_scan() {
    local network="$1"
    local ping_only="${2:-false}"
    local format="${3:-table}"
    
    local args=""
    [ -n "$network" ] && args="$args $network"
    [ "$ping_only" = "true" ] && args="$args --ping-only"
    [ "$format" != "table" ] && args="$args --format $format"
    
    eval "st_call network-scanner $args"
}

# Core scriptthing utilities

# Store utilities
st_store_get() {
    local key="$1"
    if [ -z "$key" ]; then
        st_log_error "Store get requires a key"
        return 1
    fi
    
    local result
    if result=$(PYTHONPATH=/workspace st_call "scriptthing-core-api" "store" "get" "$key" 2>/dev/null); then
        if command -v jq >/dev/null 2>&1; then
            echo "$result" | jq -r '.data.value // empty' 2>/dev/null
        else
            # Fallback without jq
            echo "$result"
        fi
    else
        return 1
    fi
}

st_store_put() {
    local key="$1"
    local value="$2"
    local ttl="$3"
    
    if [ -z "$key" ] || [ -z "$value" ]; then
        st_log_error "Store put requires key and value"
        return 1
    fi
    
    local args="store put $key $value"
    [ -n "$ttl" ] && args="$args $ttl"
    
    PYTHONPATH=/workspace st_call "scriptthing-core-api" $args >/dev/null
}

st_store_delete() {
    local key="$1"
    if [ -z "$key" ]; then
        st_log_error "Store delete requires a key"
        return 1
    fi
    
    PYTHONPATH=/workspace st_call "scriptthing-core-api" "store" "delete" "$key" >/dev/null
}

st_store_list() {
    local result
    if result=$(PYTHONPATH=/workspace st_call "scriptthing-core-api" "store" "list" 2>/dev/null); then
        echo "$result" | jq -c '.data // {}' 2>/dev/null || echo "$result"
    else
        return 1
    fi
}

# Config utilities
st_config_get() {
    local key="$1"
    local args="config get"
    [ -n "$key" ] && args="$args $key"
    
    local result
    if result=$(PYTHONPATH=/workspace st_call "scriptthing-core-api" $args 2>/dev/null); then
        if [ -n "$key" ]; then
            echo "$result" | jq -r ".data.$key // empty" 2>/dev/null || echo "$result"
        else
            echo "$result" | jq -c '.data // {}' 2>/dev/null || echo "$result"
        fi
    else
        return 1
    fi
}

st_config_home() {
    local result
    if result=$(PYTHONPATH=/workspace st_call "scriptthing-core-api" "config" "home" 2>/dev/null); then
        echo "$result" | jq -r '.data.home // empty' 2>/dev/null || echo "$result"
    else
        return 1
    fi
}

st_config_bin() {
    local result
    if result=$(PYTHONPATH=/workspace st_call "scriptthing-core-api" "config" "bin" 2>/dev/null); then
        echo "$result" | jq -r '.data.bin // empty' 2>/dev/null || echo "$result"
    else
        return 1
    fi
}

# Scripts utilities (enhanced)
st_scripts_list() {
    local result
    if result=$(PYTHONPATH=/workspace st_call "scriptthing-core-api" "scripts" "list" 2>/dev/null); then
        echo "$result" | jq -r '.data[].name // empty' 2>/dev/null || echo "$result"
    else
        return 1
    fi
}

st_scripts_get() {
    local name="$1"
    if [ -z "$name" ]; then
        st_log_error "Scripts get requires a script name"
        return 1
    fi
    
    local result
    if result=$(PYTHONPATH=/workspace st_call "scriptthing-core-api" "scripts" "get" "$name" 2>/dev/null); then
        echo "$result" | jq -c '.data // {}' 2>/dev/null || echo "$result"
    else
        return 1
    fi
}

st_scripts_create() {
    local lang="$1"
    local name="$2"
    
    if [ -z "$lang" ] || [ -z "$name" ]; then
        st_log_error "Scripts create requires language and name"
        return 1
    fi
    
    local result
    if result=$(PYTHONPATH=/workspace st_call "scriptthing-core-api" "scripts" "create" "$lang" "$name" 2>/dev/null); then
        echo "$result" | jq -r '.data.path // empty' 2>/dev/null || echo "$result"
    else
        return 1
    fi
}

# Helper function to check dependencies
st_check_dependencies() {
    local missing=""
    
    # Check if scriptthing bin directory exists
    if [ ! -d "$SCRIPTTHING_BIN_DIR" ]; then
        st_log_error "Scriptthing bin directory not found: $SCRIPTTHING_BIN_DIR"
        return 1
    fi
    
    # Check for common dependencies
    local deps="timeout"
    for dep in $deps; do
        if ! command -v "$dep" >/dev/null 2>&1; then
            missing="$missing $dep"
        fi
    done
    
    if [ -n "$missing" ]; then
        st_log_warning "Missing optional dependencies: $missing"
        st_log_warning "Some features may not work correctly"
    fi
    
    return 0
}

# Self-test function
st_self_test() {
    st_log_info "Running scriptthing shell bindings self-test..."
    
    # Check dependencies
    st_check_dependencies
    
    # Check if we can list scripts
    local scripts
    if scripts=$(st_list_scripts); then
        st_log_success "Found $(echo "$scripts" | wc -l) scriptthing scripts"
        echo "$scripts" | head -5 | while read -r script; do
            st_log_info "  - $script"
        done
    else
        st_log_error "Failed to list scriptthing scripts"
        return 1
    fi
    
    # Test a simple script call (if any scripts exist)
    if echo "$scripts" | grep -q "test-js-binaries"; then
        st_log_info "Testing script execution..."
        if st_call "test-js-binaries" >/dev/null 2>&1; then
            st_log_success "Script execution test passed"
        else
            st_log_warning "Script execution test failed (this may be normal)"
        fi
    fi
    
    st_log_success "Self-test completed"
}

# Initialize on source
st_check_dependencies >/dev/null 2>&1

# Export functions
export -f st_log_info st_log_success st_log_warning st_log_error
export -f st_script_exists st_list_scripts st_call st_call_capture st_call_json st_call_parse_json
export -f st_analyze_disk_usage st_backup_files st_csv_to_json st_query_json st_filter_logs st_network_scan
export -f st_store_get st_store_put st_store_delete st_store_list
export -f st_config_get st_config_home st_config_bin
export -f st_scripts_list st_scripts_get st_scripts_create
export -f st_check_dependencies st_self_test