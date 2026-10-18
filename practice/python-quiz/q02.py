watchlist = []
raw_lines=[]

while True:
    try:
        line = input()
    except EOFError:
        break
    
    if line.startswith("#"):
        continue
    if line.strip().startswith("WATCHLIST"):
        lable_part = line.strip()[len("WATCHLIST"):].strip()
        watchlist = [x.strip().lower() for x in lable_part.split(",")]
        
        continue
        
        
    raw_lines.append(line)    
    
def get_priority(lable,confidance,watchlist):
    
    if lable in watchlist:
        return("HIGH")
    elif confidance < 0.50 or lable == "unknown":
        return("HIGH")  
    elif 0.50 <= confidance < 0.80:
        return("MEDIUM")
    elif confidance >= 0.80 and lable != "unknown":              
        return("LOW")


for raw in raw_lines:
    last_cooma = raw.rfind(",")
    raw_lable = raw[:last_cooma]
    raw_confidence = raw[last_cooma+1:]
    try:
        confidance = float(raw_confidence.strip())
    except ValueError:
        continue      
    lable = raw_lable.strip().lower()
    
    result = get_priority(lable,confidance,watchlist)
    print(result)
          