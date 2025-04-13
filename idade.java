import java.util.Scanner;
public class idade {

	public static void main(String[] args) {
		int idade, ano = 0, mes = 0, dia = 0;
		Scanner s = new Scanner(System.in);
		
		idade = s.nextInt();
		
		ano = idade / 365;
		
		if (idade >= 365) {
			mes = (idade - (ano*365))/30;
		} else {
			mes = idade/30;
		}
		
		dia = (idade - (ano*365))%30;

		System.out.println(ano + " ano(s)");
		System.out.println(mes + " mes(es)");
		System.out.println(dia + " dia(s)");

        s.close();
		
	}

}