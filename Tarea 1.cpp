/*Codigo 1*/

#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <ctime>
using namespace std;

double vdd;
double nop;
double perc;
srand((unsigned) time(0));
int v1 = rand()%100+1;

int main()
{
    bool a[v1];

    for (int i=0; i<v1;i++)
    {
        if(a[i])
        {
            puts("T");
            vdd = vdd+1;
        }
        else {
            puts("F");
            nop = nop + 1;
        }
    }
    perc=(vdd/sizeof(a))*100;
    cout << "True: " << vdd << endl;
    cout << "False: " << nop << endl;
    cout << "% of True: " << setprecision(6) << perc << endl;
}

/*Codigo 2*/

#include <iostream>
#include <vector>

using namespace std;

string answer;

int main()
{
    vector<string> words;
    words.emplace_back("leon");
    words.emplace_back("futbol");
    words.emplace_back("comida");
    words.emplace_back("hola");

    for(int i = 0; i < words.size(); i++)
    {
        if(words[i]=="hola")
        {
            answer="La encontre!";
        }
        else
        {
            answer="No esta!";
        }
    }
    cout << "Respuesta: " << answer << endl;
}

/*Codigo 3*/

#include <iostream>

using namespace std;

int main()
{
    const char *letters[5] = { "q", "o", "k", "w", "p"};
    for(int i=4; i >=0; i--)
    {
        cout << letters[i] << endl;
    }
    return 0;
}

/*Codigo 4*/

#include <iostream>

using namespace std;

void reverse(string arr[], int start, int end)
{
    while(start<end)
    {
        basic_string<char> temp=arr[start];
        arr[start]=arr[end];
        arr[end]=temp;
        start++;
        end--;
    }
}

void printarr(string arr[], int size)
{
    for(int i=0;i<size;i++)
    {
        cout << arr[i] << " " << endl;
    }
}

int main()
{
    string arr[]={"a", "b", "c", "d", "e"};
    int n=sizeof(arr)/sizeof(arr[0]);
    printarr(arr,n);
    reverse(arr,0,n-1);
    cout << "Reversa: " << endl;
    printarr(arr,n);
    return 0;
}

/*Codigo 5*/

#include <iostream>

using namespace std;

int main()
{
    string s="I am Sleepy";
    for(char i : s)
    {
        cout << i <<endl;
    }
    return 0;
}

/*Codigo 6*/

#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    srand((unsigned) time(nullptr));
    int v1 = (rand()%100)+51;
    int v2 = (rand()%100)+51;
    int v3 = (rand()%100)+51;
    int v4 = (rand()%100)+51;
    int v5 = (rand()%100)+51;
    const char *neu[5]={ "0", "0", "0", "0", "0"};
    int arr[5]={v1, v2, v3, v4, v5};
    for(int i=0;i<5;i++)
    {
        if(arr[i]>=100)
        {
            neu[i]="T";
        }
        else
        {
            neu[i]="F";
        }
    }
    for(auto & j : neu)
    {
        cout << j << endl;
    }
}

/*Codigo 8*/

#include <iostream>
using namespace std;

int main()
{
    int a,n;
    int count=0;
    int sum=0, avg;
    int arr[10];
    cout<< "Ingrese 10 numeros enteros: ";
    for(int & i : arr)
    {
        cin >> a;
        i=a;
    }
    n=sizeof(arr)/sizeof(arr[0]);
    for(int j=0;j<n;j++)
    {
        sum+=arr[j];
        avg=sum/n;
    }
    for(int k : arr)
    {
        if(k>avg)
        {
            count++;
        }
        else
        {

        }
    }
    cout << "Numbers above average: " << count << endl;
    cout << "The average is: " << avg << endl;
    return 0;
}

/*Codigo 9*/

