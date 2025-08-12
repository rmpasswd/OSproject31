# osproject31
CPU Scheduling Algorithms with GUI

## Demo
![GIF Demo]( https://github.com/rmpasswd/rmpasswd/blob/main/osproject31.demo.gif)
<img width="797" height="720" alt="image" src="https://github.com/user-attachments/assets/551b1fc6-6580-44cf-b1d3-af9ea4d11cf4" />  
<img width="781" height="152" alt="image" src="https://github.com/user-attachments/assets/c7462c86-09a4-4fe1-8d96-78b654961f47" />  
Selecting "All" will return the algorithm the least average turnaround time, in this example:
<img width="790" height="718" alt="image" src="https://github.com/user-attachments/assets/e12ad4af-7196-456b-a2e6-5eaaf78085c2" />



## Installation

Execute the following commands:
The GUI is written with PyQt5. So, PyQt5 will be installed(~50 MB). 
```
git clone https://github.com/rmpasswd/osproject31.git
cd osproject31
pip install -r requirements.txt
python ./design.py
```

## Possible Errors:
When trying to install dependency:  
<img width="903" height="171" alt="image" src="https://github.com/user-attachments/assets/3090006c-e2e6-4920-aba5-c42c085a38b2" />  
Fix:  
Instead of `py -m pip install PyQt5==5.15.4`, run `pip install -r PyQt5`


