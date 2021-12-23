#!/usr/bin/env python3
from contextlib import nullcontext
import requests
import sys
from time import sleep
import re
from datetime import datetime
import argparse

class Comb:
    print('\n',str(datetime.now()))
    print('--------------------------\n')
    sleep(2)
    link=''
    Res=[]
    status=[]
    url=[]
    link2=[]
    Comb=[]
    x=0
    domain=''
    file=''
    @staticmethod
    def Combinations(domain,file):
        Comb.domain=domain
        Comb.file=file
        with open(file,'r')as f:
            link=f.readlines()
            print("link is",link)
            Comb.comb="".join(link)

            print("The second link is: ",Comb.comb)
            i=0
            for i in link:
                if "".join(link)=='\n' or "".join(link)=='/' or "".join(link)==' ':
                    Comb.comb.pop(i)
        for i in range(0,len(link)):
            Comb.comb=('http://',domain,'/',link[i])
            Comb.x=Comb.x+1     #number of linkes
            x="".join(Comb.comb)
            Comb.link2.append(x)
        Comb.link="".join(Comb.link2)
        print("The Var Link")
        print(Comb.link)
    @staticmethod
    def Reqest(time):
        print ("In the request: ")

        i=0
        for i in range(0,len(Comb.link2)):
            try:
                sleep(time)
                response = requests.get(Comb.link2[i])
                Comb.Res=response
                print('-',Comb.link2[i])
                print ("The web resource Successfully responded \n")
                print(response.status_code)
                Comb.status=response.status_code
                print(response.url,"\n")
                Comb.url=response.url
                Comb.output()
            except Exception as e:
                #print(i,e,'\n')
                print(i,"- ",Comb.link2[i],"\n","The host isn't reachable maybe it's a link for API or not a valid link","\n")
                with open('Errors.txt','w')as f:
                    f.write(str(datetime.now()))
                    f.write("\n--------------------------")
                    f.write('\n\n')
                    for i in range(0,len(Comb.link2)):
                        f.write("The Url provided isn't reachable: ")
                        f.write(Comb.link2[i])
        now = datetime.now()
        current_time1 = now.strftime("%H:%M:%S")
        print("Current Time =", current_time1)
    def output():
        with open('Results.txt','w')as f:
            f.write(str(datetime.now()))
            f.write("\n--------------------------")
            f.write("\n\n")
            for i in range(0,len(Comb.link2)):
                f.write(i+1)
                f.write('-')
                f.write(str(Comb.status[i]))
                f.write('- ')
                f.write(Comb.url[i])
                f.write('The prignal url is: ')
                f.write(Comb.link2[i])
                f.write('\n')

def main():

    parser=argparse.ArgumentParser()
    parser.add_argument("-l","--WordList",help="Enter the path of the wordlist",type=str)
    parser.add_argument("-d","--DelayTime",help="Enter the Delay Time Default=0.7 S",type=float,default=0.7)
    parser.add_argument("IP",help="The IP or the name of the WebSite",type=str)
    args=parser.parse_args()
    s=Comb()

    
    try:
        s.Combinations(args.IP,args.WordList)
    except Exception as e:
        print("Using the Default WordList: /usr/share/seclists/Discovery/DNS/subdomains-top1million-*.txt")
        s.Combinations(args.IP,"/usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt")
    except Exception as e:
        print(e)
    s.Reqest(args.DelayTime)
if __name__=="__main__":
    main()