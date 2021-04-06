import java.lang.*;
import java.util.*;
import java.io.*;

class Solution{
	public static void main(String[] args){
		int[] arr = {1,1};
		Solution sc = new Solution();
		// sc.fiboItr(arr,5);
		System.out.printf("1 1 ");
		sc.fiboRec(1,1,5,2);
	}
	void fiboRec(int a, int b, int l, int i){
		if(i>=l) return;
		System.out.printf("%d ",a+b);
		// System.out.printf("%d ",i);
		i=i+1;
		this.fiboRec(b,a+b,l,i);
	}
	void fiboItr(int[] arr, int l){
		int a = arr[0];
		int b = arr[1];
		System.out.printf("%d %d ",a,b);
		for(int i=2; i<l; i++){
			int c =a+b;
			System.out.printf("%d ",c);
			a=b;
			b=c;
		}
	}
}