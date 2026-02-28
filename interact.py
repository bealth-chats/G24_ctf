import pexpect
import sys

child = pexpect.spawn('./vault', encoding='utf-8')
child.expect(r'\$', timeout=10)
child.sendline('auth ' + 'A' * 200)
child.expect(pexpect.EOF, timeout=15)
print(child.before)
