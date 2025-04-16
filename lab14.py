#v1

def main():
    dict_1, dict_2 = {"a": 500, "b": 600}, {"c": 100, "d": 200}

    dict_1.update(dict_2)
    dict_1['e'] = 1000

    print(dict_1)

if __name__ == "__main__":
    main()