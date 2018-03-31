이 프로젝트는 비가 오는 날 창문이 열려있으면 창문을 닫아 내부에 비가 들어오는 것을 막아주기 위한 것입니다.
This project is to prevent rain from falling inside if it's raining and the window is open.

빗물 감지 센서를 이용해 비가 오는지 감지합니다.
It detects the rain using Raindrops sensor.

빗물 감지 센서의 output 값이 0이면 비가 오는 것이고 1이면 비가 오지 않는 것입니다.
If Raindrops sensor's Output is 0, It's raining.
If Raindrops sensor's Output is 1, It isn't raining.

비를 감지하면서 창문이 열려있으면 모터를 90도 회전시켜 창문을 닫아줍니다.
비가 오지 않으면서 창문이 닫혀있으면 모터를 -90도 회전시켜 창문을 열어줍니다.
창문을 열고 닫는 것을 구현하기에는 무리가 있어 창문의 개폐 여부를 알 수 있는 방법은 버튼으로 대체했습니다.
버튼이 눌려있으면 창문이 열려있는 것이고 눌려있지 않으면 창문이 닫혀있는 것입니다.
The motor is used to open and close windows.
If it's raining and the window is open, Turn the motor 90 degrees to close the window.
If it isn't raining and the window is closed, Turn the motor -90 degrees to open the window.
Opening and closing the window has not been realized.
So, I replaced it with a button.
