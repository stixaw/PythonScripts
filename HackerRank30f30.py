Hanker Rank Day 3 of 30 C# Solution:
    public static void isNumberWeird(int num){
        
        if ((num % 2 == 1) || (num >= 6 && num <= 20))
        {
            Console.WriteLine("Weird");
        }
        else
        {
            Console.WriteLine("Not Weird");
        }
    }
	
	
	# Python 2

n = int(raw_input().strip())

if n % 2 == 0 and (n < 6 or n > 20):
    print "Not",
print "Weird"