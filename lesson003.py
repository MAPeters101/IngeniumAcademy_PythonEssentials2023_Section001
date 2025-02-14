
if __name__ == '__main__':
    string = "Python"
    print(string[0])

    # Slicing
    print(string[1:4])
    print(string[::2])

    # Immutability
    #string[0] = "C"

    string = "Not Python"
    print(string)

    # Formatted strings
    job = 'Software Developer'

    print(f"If you learn Python you can be a {job}")

    print("If you learn Python you can be a {job}".format(job=job))





