def main():
    try:
        1 / 0  # ZeroDivisionError: division by zero
    except ZeroDivisionError as ex:
        print(ex)


if __name__ == '__main__':
    main()
