import json
import sys

data = json.load(sys.stdin)
for build in data.get('builds', []):
    print(f"Build ID: {build['id']}")
    print(f"Build Script: {build['build_script']}")
    print("Log output:")
    print(build['log_output'])
    print("-" * 40)
