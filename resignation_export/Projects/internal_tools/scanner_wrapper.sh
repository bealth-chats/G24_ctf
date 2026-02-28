#!/bin/bash
# Quick wrapper for internal vulnerability scanner
# Usage: ./scanner_wrapper.sh <target> [profile]

TARGET="${1:?Usage: $0 <target> [profile]}"
PROFILE="${2:-default}"

echo "[$(date)] Running scan: target=${TARGET} profile=${PROFILE}"
python3 /opt/cyberleap/tools/scanner.py "${TARGET}" "${PROFILE}"
echo "[$(date)] Scan complete"
