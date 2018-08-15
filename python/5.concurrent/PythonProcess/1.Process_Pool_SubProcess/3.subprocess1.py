import subprocess


def main():
    result = subprocess.run(["ping", "www.baidu.com"])
    print(result.stdout)


if __name__ == '__main__':
    main()