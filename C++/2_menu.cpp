#include <windows.h>
#include <iostream>

#define _file_menu_new 1   //เปลี่ยนชื่อเพื่อให้ไม่สับสนเวลาเอาไปใส่ case
#define _file_menu_open 2  //            "
#define _file_menu_close 3 //            "

#define _yes_press 4
#define _no_press 5

LRESULT CALLBACK _windowprocedure(HWND _hwnd, UINT _mes, WPARAM _wp, LPARAM _lp); 

void _addmenu(HWND); //Pototype สำหรับใส่เมนู

HMENU _hmenu; //น่าจะเป็นวินโดร์ หรือ Root ใน PY

int WINAPI WinMain(HINSTANCE _hinst, HINSTANCE _hprevinst, LPSTR _args, int _ncmdshow)
{
    WNDCLASSW _wc = {0};
    
    _wc.hbrBackground = (HBRUSH) COLOR_WINDOW; 
    _wc.hCursor = LoadCursor(NULL,IDC_IBEAM);
    _wc.hInstance = _hinst;
    _wc.lpszClassName = L"my_windows_class"; 
    _wc.lpfnWndProc = _windowprocedure;

    if(!RegisterClassW(&_wc)) return -1;

    CreateWindowW(
        L"my_windows_class",
        L"GUI_TUTORIAL", 
        WS_OVERLAPPEDWINDOW | WS_VISIBLE,
        100, 
        100, 
        500, 
        400, 
        NULL,
        NULL,
        NULL,
        NULL
    ); 
    
    MSG _msg = {0};

    while (GetMessage(&_msg,NULL,0,0))
    {
        TranslateMessage(&_msg);
        DispatchMessage(&_msg);
    }

    return 0;
}

LRESULT CALLBACK _windowprocedure(HWND _hwnd, UINT _msg, WPARAM _wp, LPARAM _lp)
{
    switch (_msg)
    {
    case WM_COMMAND: //ตรวจว่ากดปุ่ม
        switch(_wp) //ดูว่าปุ่มที่กดคือปุ่มอะไร
        {
            case _file_menu_close:
                DestroyWindow(_hwnd); //ปิด Menu
                break;
            case _file_menu_open:
                std::cout << "open_menu clicked\n"; //ให้ทำอะไร
                break;
            case _yes_press:
                std::cout << "you_press_yes\n";
                break;
            case _no_press:
                std::cout << "you_press_no\n";
                break;
        }

    case WM_CREATE: // case นี้เพิ่มในหัวข้อ _2 เวลาสร้างก็ให้สร้าง Menu มาด้วย
        _addmenu(_hwnd);
        break;

    case WM_DESTROY: 
        PostQuitMessage(0);
        break;
    
    default:
        return DefWindowProcW(_hwnd, _msg, _wp, _lp);
    }

    return 0;
}

void _addmenu(HWND _hwnd) //มาใหม่
{
    _hmenu = CreateMenu();
    HMENU _hfilemenu = CreateMenu();

    HMENU _hsubmenu_help = CreateMenu();
    HMENU _hsubmenu_help2 = CreateMenu();
    
    /*AppendMenu 
    (
        ชื่อแถบเมนูที่จะให้อยู๋(มั้ง),
        รูปแบบ, //EX MF_STRING = กดได้อย่างเดียว MF_POPUP = มีเมนูย่อย
        รหัส (ให้ส่งอะไรเข้า Switchcasw callback),
        จะให้เขียนอะไรที่ปุ่ม
    
    )*/
    //รายละเอียดเพิ่มเติม https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-appendmenua

    AppendMenuA(_hfilemenu,MF_STRING,_file_menu_new,"New");
    AppendMenuA(_hfilemenu,MF_STRING,_file_menu_open,"Open");
    AppendMenuA(_hfilemenu,MF_SEPARATOR,0,NULL); //ทำให้มันมีข่องที่เป็นเส้น
    AppendMenuA(_hfilemenu,MF_STRING,_file_menu_close,"Close");

    AppendMenuA(_hmenu,MF_POPUP,
    (UINT_PTR)_hfilemenu, // กดแล้วเรียกเมนูย่อยต่อ
    "File");

    AppendMenuA(_hsubmenu_help2,MF_STRING,_yes_press,"Yes");
    AppendMenuA(_hsubmenu_help2,MF_STRING,_no_press,"No");

    AppendMenuA(_hsubmenu_help,MF_POPUP,(UINT_PTR)_hsubmenu_help2,"Need Help?");
    AppendMenuA(_hmenu,MF_POPUP,(UINT_PTR)_hsubmenu_help,"Help");

    SetMenu(_hwnd, _hmenu);
}