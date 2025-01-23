#include <bits/stdc++.h>
#include <array>
using namespace std;

void first_fit(vector<int> process, vector<int> memory){
    int i=0,j=0;
    vector<int> temp={0,0,0,0,0};
    for ( i=0;i<4;i++){
        int flag=0;
        for (j=0;j<memory.size();j++){
            if (process[i]<=memory[j] && temp[j]==0){
                cout<<"memory "<<memory[j]<<" is allocated to process "<<process[i]<<endl;
                memory[j]=0; temp[j]=1;
                flag=1;
                break;
            }
        }
            if (flag==0)cout<<process[i]<<" is not allocated any memory"<<endl;
    }
}


void worst_fit(vector<int> process, vector<int> memory){
    vector<int> temp(memory.size(), 0);
    for (int i = 0; i < process.size(); i++) {
        int bestFitIndex = -1;
        for (int j = 0; j < memory.size(); j++) {
            if (process[i] <= memory[j] && (bestFitIndex == -1 || memory[j] > memory[bestFitIndex]) && temp[j] == 0) {
                bestFitIndex = j;
            }
        }
        if (bestFitIndex != -1) {
            cout << "Memory " << memory[bestFitIndex] << " is allocated to process " << process[i] << endl;
            temp[bestFitIndex] = 1;
        } else {
            cout <<"process "<< process[i] << " is not allocated any memory" << endl;
        }
    }
}


void best_fit(vector<int> process, vector<int> memory){
    vector<int> temp(memory.size(), 0);
    for (int i = 0; i < process.size(); i++) {
        int bestFitIndex = -1;
        for (int j = 0; j < memory.size(); j++) {
            if (process[i] <= memory[j] && (bestFitIndex == -1 || memory[j] < memory[bestFitIndex]) && temp[j] == 0) {
                bestFitIndex = j;
            }
        }
        if (bestFitIndex != -1) {
            cout << "Memory " << memory[bestFitIndex] << " is allocated to process " << process[i] << endl;
            temp[bestFitIndex] = 1;
        } else {
            cout <<"process "<< process[i] << " is not allocated any memory" << endl;
        }
    }
}

int main()
{
    vector<int> process = {212, 417, 112, 426};
    vector<int> memory = {100, 500, 200, 300, 600};
    first_fit(process, memory);
    cout<<"best_fit"<<endl;
    sort(memory.begin(),memory.end());
    best_fit(process, memory);
    cout<<"worst_fit"<<endl;
    worst_fit(process, memory);
    return 0;
}