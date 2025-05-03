#IT3883/W02
#Nornu Ninayor
#Final Exam
#05/03/25
#It also includes error handling to prevent crashes from invalid inputs.
#Resources used W3chool,youtube,& google,lecture notes


#Convert the words into numbers
coin_value = { #naming the value, since we are taking about money i put coins.
"pennies":0.01, #unit decides to places them from smallest to greatest because thats what made sense
"nickels":0.05, #was spelling nickels wrongs,giving me the wrong output
"dimes":.10,
"quarters":.25
}
def convert_words_into_value(sentence):# this lines makes sure that sentnces written is read by python
    total_value=0.0 #this is stating the value.0.0 represent money
    words=sentence.lower().split() #this is to stop syntax sensitivity, python should still be able to read lowercase sentences.
    
    for i in range(len(words)):
       if words[i].isdigit():
          quantity= int(words[i])
          coin=words[i+1]
          
          if coin=="penny":
              coin="pennies"   #so this will account for singular and pluar inputs that are given.
          elif coin=="nickel":
              coin="nickels"
          elif coin=="dime":
              coin="dimes"
          elif coin=="quarter":
              coin="quarters"
                  
          if coin in coin_value:
             total_value+= quantity*coin_value [coin]#want the code to able to caluculate things like 7 quaters. it will do the match and hopefully show the right input
            
    print(round(total_value, 2))
 #we want the code to round to the nearest hundreth because thats how standard money is

    
#Code should automatically show the number form of the sentences written.
