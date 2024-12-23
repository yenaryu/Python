import ctypes

# Windows API를 사용하기 위해 필요한 설정
kernel32 = ctypes.windll.kernel32
hConsole = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE = -11


text = "Hello World\n"  # 출력 텍스트
text_buffer = ctypes.create_unicode_buffer(text)
length = len(text)  # 텍스트 길이 (문자 수)

# WriteConsoleW API를 호출하여 텍스트 출력
written = ctypes.c_ulong(0)

success = kernel32.WriteConsoleW(
    hConsole,
    text_buffer,  # 출력할 텍스트 버퍼
    length,  # 출력할 텍스트 길이
    ctypes.byref(written),  # 출력된 문자 수를 저장할 포인터
    None,
)
