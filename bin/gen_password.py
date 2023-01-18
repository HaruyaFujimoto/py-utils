## source
## https://gammasoft.jp/blog/generate-password-by-python/

import string
import secrets
import sys

def main():
    n = 12
    args = sys.argv
    if len(args) >= 2:
        n = int(args[1])
    print(f"number of caracters: {n}")
    pass_string = pass_gen(n)
    print(pass_string)

def pass_gen(size=12):
   chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
   # 記号を含める場合
   # chars += '%&$#()'

   return ''.join(secrets.choice(chars) for x in range(size))

if __name__ == "__main__":
    main()
