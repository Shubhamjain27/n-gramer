import sys, json;

def read_in():
    input=sys.stdin.readlines();

    return json.loads(input[0]);
    #return {"height":"15", "weight":"21", "shoeSize":"31"};

def main():
    input = read_in();
    
    height = float(input["height"]);
    weight = float(input["weight"]);
    shoeSize = float(input["shoeSize"]);

    result = classification(height, weight, shoeSize);

    print(result);

def classification(height, weight, shoeSize):

    Percentage = height+weight+shoeSize;
    Sex = "Male" if (Percentage>50) else "Female";
    result=json.dumps({"Sex": Sex, "Percentage": Percentage});

    return result;


if __name__ == '__main__':
    main()