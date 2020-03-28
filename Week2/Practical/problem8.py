text = input("The given text:  ")
start_index = input("Start index: ")
end_index = input("End index: ")
x = text[int(start_index): int(end_index) :1]
print("Output string:", x)