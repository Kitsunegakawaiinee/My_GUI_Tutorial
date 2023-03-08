#include <windows.h>

//ตัวที่มี _ข้างหน้าคือตัวที่บอกว่าสามารถเปลี่ยนชื่อได้ตามใจชอบ

LRESULT CALLBACK _windowprocedure(HWND _hwnd, UINT _mes, WPARAM _wp, LPARAM _lp); //prototype

int WINAPI WinMain(HINSTANCE _hinst, HINSTANCE _hprevinst, LPSTR _args, int _ncmdshow)
{
    WNDCLASSW _wc = {0};

    _wc.hbrBackground = (HBRUSH) COLOR_WINDOW; 
    //color https://social.msdn.microsoft.com/Forums/vstudio/en-US/e4fd1c4b-4407-4743-a74f-7d78338c17d2/hbrbackground-hbrushcolorwindow1-what-is-1-for?forum=vcgeneral
    _wc.hCursor = LoadCursor(NULL,IDC_IBEAM);
    //ดูรหัสจาก https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadcursora
    _wc.hInstance = _hinst;

    _wc.lpszClassName = L"my_windows_class"; //ตั้งเองได้

    _wc.lpfnWndProc = _windowprocedure;

    if(!RegisterClassW(&_wc)) return -1;

    CreateWindowW(
        L"my_windows_class",
        L"GUI_TUTORIAL", //title
        WS_OVERLAPPEDWINDOW | WS_VISIBLE,
        //style https://learn.microsoft.com/en-us/windows/win32/winmsg/window-styles
        100, //x
        100, //y
        //อยู่ตรงไหน (นับบนซ้ายเป็น) 0,0
        500, //กว้าง
        400, //สูง
        NULL,
        NULL,
        NULL,
        NULL
    );
    //สร้างวินโดว์ https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createwindowa
    //เขียนบรรทัดเดียวก็ได้แต่จะดูยากหน่อย

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
    case WM_DESTROY: //ถ้ากดปุ่มปิด
        PostQuitMessage(0);
        break;
    
    default:
        return DefWindowProcW(_hwnd, _msg, _wp, _lp);
    }

    return 0;
}
