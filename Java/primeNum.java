import java.util.Scanner;
import java.lang.*;
import java.io.*;

class Solution{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		Solution sl = new Solution();
		int num = sc.nextInt();
		System.out.println(sl.isPrime(num));
	}
	boolean isPrime(long n){
		if(n<=3) return true;
		if(n%2==0) return false;
		for(int i=3; i<=Math.sqrt(n); i+=2){
			if(n%i==0)
				return false;
		}
		return true;
	}
}