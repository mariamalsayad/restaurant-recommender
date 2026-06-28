
ques = input("Hi I will ask you a couple of questions \nto identify the best restaurant that suits you the most. Enter yes to continue or no to exit: ")



def recommend():
    #fastfood dishes
    Kfc = ["fried chicken", "poutine"]
    Vonns = ["burgers", "cheesesteak", "nashville fried chicken"]

    paramount = ["shish tawouk", "mixed grill", "beef skewers", "kofta"]
    uncleshawrma = ["chicken shawarma", "beef shawarma"]
    #italian dishes
    spaghettifacttory = ["manicotti", "penne with chicken", "steamed mussels", "pesto penne", "calamari fritti"]
    #japaneese dishes
    sushimura = ["sushi", "seafood udon", "sashimi rolls", "shrimp tempura", "salmon gamma"]
    #indian dishes
    karakoram = ["chicken biryani", "lamb biryani", "butter chicken", "lamb buhna", "Gulabjamun (I reccomend this desert)"]
    swanindiankitchen = ["tandori roti", "chicken tikka", "samosa"]
  
    #get user's favourite cusine
    food_type = input(
        "What is your favorite type of food:\n a) Fast food\n b) Lebanese\n c) Italian\n d) Japaneese\n e) Indian: ")
    
   

    if food_type.strip() == "a":
        print("Available dishes for Fast Food: ", Vonns + Kfc)
    
    elif food_type.strip() == "b":
        print("Available dishes for Lebanese: ", paramount + uncleshawrma)
    
    elif food_type.strip() == "c":
      print("Avaialble dishes for Italian: ", spaghettifacttory)
   
    elif food_type.strip() == "d":
      print("Availble dishes for Japaneese: ", sushimura)

    elif food_type.strip() == "e":
      print("Alert: The BEST Indian cusines are ONLY available in Vancouver and indoors and spicy")
      print("Availble dishes for indian: ", karakoram + swanindiankitchen)

    else:
        print("I don't know your preferred dishes for this food type.")
        return

    dish = input("What is your favorite dish from the list above? ")
    spicy = input("Do you like it spicy or mild:\n a) Spicy\n b) Mild: ")
    location = input("Would you like to go eat in:\n a) Vancouver\n b) Richmond: ")
    setting = input("Lastly, do you like eating:\n a) Outdoors\n b) Indoors: ")
  

    if (
        food_type.strip() == "a"
        and dish.lower().strip() in Vonns
        and spicy.strip() in ["a", "b"]
        and location.strip() == "a"
        and setting.strip() in ["a", "b"]
    ):
      print("Vonn's is recommended for its mouthwatering burgers. You must try their cheesesteak!")

    elif (
      food_type.strip() == "a"
        and dish.lower().strip() in Kfc 
        and spicy.strip() in ["a", "b"]
        and location.strip() in ["a", "b"]
        and setting.strip() in ["a", "b"]
    ):
      print("i recommned kfc for its simple yet delcious friedchicken buckets.")
      

    elif (
        food_type.strip() == "b"
        and dish.lower().strip() in paramount 
        and spicy.strip() in ["a", "b"]
        and location.strip() == "a"
        and setting.strip() == "b"
    ):
        print("Paramount is recommended for its exceptional seasonings of Lebanese cuisine")
    
    elif (
      food_type.strip() == "b"
      and dish.lower().strip() in uncleshawrma 
      and spicy.strip() in ["a", "b"]
      and location.strip() == "b"
      and setting.strip() == "b"
    ):
      print("Uncle Sal's Shawarma Restaurant is a top pick for its delicious chicken and beef shawarma. You MUST try their chicken shwarma plate")
  
    elif (
      food_type.strip() == "c"
      and dish.lower().strip() in spaghettifacttory
      and spicy.strip() in ["a", "b"]
      and location.strip() in ["a", "b"]
      and setting.strip() in ["a", "b"]
    ):
      print("Spaghetti Factory is a top pick for its amazing spaghettie and its cozy/homely Italian dining experience")
  
    elif (
      food_type.strip() == "d"
      and dish.lower().strip() in sushimura
      and spicy.strip() in ["a", "b"]
      and location.strip() in ["a", "b"]
      and setting.strip() == "b"
    ):
        print("Sushi Mura is recommended, featuring fresh and melt-in-your-mouth sushi")
      
   
    elif (
        food_type.strip() == "d"
        and dish.lower().strip() in sushimura
        and spicy.strip() in ["a", "b"]
        and location.strip() in ["a", "b"]
        and setting.strip() == "a"):
          print("sorry cannot recommendm a restraunt, Sushi Mura has indoor settings only, try agian.")
   
    elif (
        food_type.strip() == "e"
        and dish.lower().strip() in karakoram
        and spicy.strip() == "a"
        and location.strip() == "a"
        and setting.strip() == "b"):
          print("Karakoram is recommended, featuring the original and rich flavours and spices of indain dishes. You must try their desert")
      
 
    elif (
      food_type.strip() == "e"
      and dish.lower().strip() in karakoram or  swanindiankitchen
      and spicy.strip() in ("a", "b")
      and location.strip() == "b"
      and setting.strip() in ("a","b")
    ):
        print("Cannot recommend restraunts, good Indian cusines are all spicy, indoors, and in Vancouver!")
      
    elif (
        food_type.strip() == "e"
        and dish.lower().strip() in swanindiankitchen
        and spicy.strip() in ["a", "b"]
        and location.strip() == "a"
        and setting.strip() == "b"):
          print("Swad Indian Kitchen Is recommended for its comfy and friendly seatings")
   
    else:
        print("sorry i dont have a reccomendation for you. Try again with different prefrences.")

if ques.lower() == "yes":
    recommend()

if ques.lower() == "no":
  print("ok, bye.")
