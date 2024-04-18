from Parser import parse, write_to_excel

if __name__ == '__main__':
    data = parse()
    write_to_excel(data)
