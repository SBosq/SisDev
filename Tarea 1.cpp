/*Codigo 1*/

#include <iostream>
#include <cstdlib>
#include <iomanip>
using namespace std;

double vdd;
double nop;
double perc;
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

#include <iostream>
#include <cstdlib>
using namespace std;
int v1 = rand()%51;

int main()
{
    int a[v1];
    int max=a[0];
    int count=1;
    for (int i=0; i<v1;i++)
    {
        if(a[i]>a[i])
        {
            max=a[i];
            count=1;
        }
        else
        {
            count++;
        }
    }
    cout<< "Max number found in the array: " << max << endl;
    cout<< "Number of instances that number appears: " << count << endl;
}

/*Codigo 10*/

#include <iostream>
using namespace std;

int main()
{
    cout << "Write the scores of the students: " << endl;
    int count=0;
    int count1=0;
    int count2=0;
    int sum=0, avg;
    int input;
    int num[100];
    for(int i=0;i<100;i++)
    {
        cin >> input;
        if(input>0)
        {
            count++;
            num[i]=input;
        }
        else
            break;
    }
    int n=count;
    for(int j=0;j<n;j++)
    {
        sum+=num[j];
        avg=sum/n;
    }
    for(int k : num)
    {
        if(k>=avg && k<10)
        {
            count2++;
        }
        else if (k<avg && k<10)
        {
            count1++;
        }
    }
    cout << "Numbers at/above average: " << count2 << endl;
    cout << "Numbers below average: " << count1 << endl;
    cout << "The average is: " << avg << endl;
    return 0;
}

/*Codigo 11*/

#include <iostream>
using namespace std;

int main()
{
    int num[100];
    int neu[100];
    int input;
    int counter=0;
    cout << "Enter numbers to be entered into an array: ";
    for(int & i : num)
    {
        cin >> input;
        i=input;
    }
    for(int i=0; i<5;i++)
    {
        bool found=false;
        for(int j=0;j<counter;j++)
        {
            if (num[i]==neu[j])
            {
                found=true;
                break;
            }
        }
        if (!found)
        {
            neu[counter++]=num[i];
        }
    }
    return 0;
}

/* Codigo 12 */

#include <iostream>
using namespace std;

int main()
{
    int num[100];
    int count0=0;
    int count1=0;
    int count2=0;
    int count3=0;
    int count4=0;
    int count5=0;
    int count6=0;
    int count7=0;
    int count8=0;
    int count9=0;
    for(int i=0;i<100;i++)
    {
        num[i]=rand()%10;
    }
    for (int i = 0; i < 100; ++i)
    {
        int tmp=num[i];
        switch (tmp)
        {
            case 0:
                count0++;
                break;
            case 1:
                count1++;
                break;
            case 2:
                count2++;
                break;
            case 3:
                count3++;
                break;
            case 4:
                count4++;
                break;
            case 5:
                count5++;
                break;
            case 6:
                count6++;
                break;
            case 7:
                count7++;
                break;
            case 8:
                count8++;
                break;
            case 9:
                count9++;
                break;
        }
    }
    cout<<"0s in the array: "<<count0<<endl;
    cout<<"1s in the array: "<<count1<<endl;
    cout<<"2s in the array: "<<count2<<endl;
    cout<<"3s in the array: "<<count3<<endl;
    cout<<"4s in the array: "<<count4<<endl;
    cout<<"5s in the array: "<<count5<<endl;
    cout<<"6s in the array: "<<count6<<endl;
    cout<<"7s in the array: "<<count7<<endl;
    cout<<"8s in the array: "<<count8<<endl;
    cout<<"9s in the array: "<<count9<<endl;
    
    return 0;
}

/* Codigo 13 */

#include <iostream>
using namespace std;

int average(int array[])
{
    int sum=0;
    int avg;
    for (int i = 0; i < 6; i++)
    {
        sum+=array[i];
        avg=sum/6;
    }
    return avg;
}

double average(double array[])
{
    double sum=0;
    double avg;
    for (int i = 0; i < 6; ++i)
    {
        sum+=array[i];
        avg=sum/6;
    }
    return avg;
}

int main()
{
    int arr[]={1, 2, 3, 4, 5, 6};
    cout << average(arr) << endl;

    double arr1[]={6.0, 4.4, 1.9, 2.9, 3.4, 3.5};
    cout << average(arr1) << endl;
}

/* Codigo 14 */
