import sys

hosts = ''
for i in range(2,len(sys.argv)):
    hosts += sys.argv[i]+' '

content = '''127.0.0.1\tlocalhost\n127.0.1.1\tkali\n::1\t\tlocalhost ip6-localhost ip6-loopback\nff02::1\t\tip6-allnodes\nff02::2\t\tip6-allrouters\n\n'''

content += sys.argv[1] + '\t' + hosts + '\n'
f = open('/etc/hosts', 'w')
f.write(content)
