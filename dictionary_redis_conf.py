import redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
def load_into_redis(file_path):
    with open(file_path, 'r', newline='') as file:
        for row in file:
            k_v_list = row.split(",")
            r.set(k_v_list[0], "".join(k_v_list[1:]))



load_into_redis("Shakespeare_glossary_dict.csv")



print(r.get("ANGEL"))