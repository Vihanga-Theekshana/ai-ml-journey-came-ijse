values = []
threshold = None

while True:
    try:
        value = input()
    except EOFError:
        break
    
    line =value
    
    if line.strip() == "":
        continue
    if line.startswith("#"):
        continue
    
    if line.startswith("DROP below="):
        try:
            threshold = float(line[len("DROP below="):])
        except ValueError:
            pass
        continue
    try:
        number = float(line)
        values.append(number)
    except ValueError:
        print(f"skipped {line}") 
        
if threshold is not None:
    final_list = [value for value in values if value >= threshold ]
else:
    final_list = [value for value in values ]

if not final_list:
    print("no valied values")
else:
    print(final_list)            
    avg = sum(final_list)/len(final_list)
    print(f"\naverage:{avg:.3f}")
    
    
             
    
              