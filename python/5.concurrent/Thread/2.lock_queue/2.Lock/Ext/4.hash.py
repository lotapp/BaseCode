from hashlib import sha1
from multiprocessing.dummy import Lock

m_lock = Lock()
z_lock = Lock()
print(f"是否相等：{m_lock==z_lock}\n{m_lock}\n{z_lock}")  # 地址不一样

m_code = hash(m_lock)
z_code = hash(m_lock)
print(f"是否相等：{m_code==z_code}\n{m_code}\n{z_code}")  # 值一样

# Java可以使用：identityhashcode
m_code = sha1(str(m_lock).encode("utf-8")).hexdigest()
z_code = sha1(str(z_code).encode("utf-8")).hexdigest()
print(f"是否相等：{m_code==z_code}\n{m_code}\n{z_code}")  # 不相等

m_code = id(m_lock)
z_code = id(z_lock)
print(f"是否相等：{m_code==z_code}\n{m_code}\n{z_code}")  # 不相等
