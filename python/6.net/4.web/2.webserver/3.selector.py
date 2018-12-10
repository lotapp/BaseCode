import selectors

# Linux下使用epoll，Win下使用select
Selector = selectors.DefaultSelector()

# selectors.EVENT_READ
# selectors.EVENT_WRITE
