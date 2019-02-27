import redis


def main():
    try:
        conn = redis.Redis(host="192.168.36.123", port=6379, password="dntdnt")
        conn.set("name", "hello")
        if conn.exists("name"):
            result = conn.get("name")
            print(result)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
