#include <math.h>
#include <stdio.h>
int checktriangle(int a, int b, int c)
{
    int A, B, C;
    if ((c < a + b) && (b < a + c) && (a < c + b))
    {
        if (a == b && a == c)
        {
            printf("Triangulo equilatero \n");
        }
        else if (a == b || b == c)
        {
            printf("Triangulo isosceles \n");
        }
        else
        {
            printf("Triangulo escaleno \n");
        }
    }
    else
    {
        printf("No es un triangulo \n");
    }
    return 0;
}
int main()
{
    int a, b, c, i, n;
    printf("Numero de casos de prueba: \n");
    scanf("%d", &n);
    printf("%d", n);
    printf("\n");
    for (i = 1; i < n + 1; i++)
    {printf ("Marcar los valores de longitud de los lados del triangulo (uno por linea): 
\n"); 
scanf ("%d", &a); printf ("%d,", a); 
scanf ("%d", &b); printf ("%d,", b); 
scanf ("%d", &c); printf ("%d: \n", c); 
checktriangle (a, b, c);
    };
    return 0;
}