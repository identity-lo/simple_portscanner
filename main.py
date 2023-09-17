import flet as ft 
import socket

def main(page : ft.page):
    page.title = "Port Scanner"
    
    def Port_Scanner(e):
        host = socket.gethostbyname(urlbar.value)
        try : 
            for port in range(int(rangebar.value)):
                s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((host , port))
                if result == 0:
                    list_view.controls.append(ft.Text(value=f"[+] TCP is open {host}:{port}" , color=ft.colors.GREEN_300))
                    page.update()
                else:
                    list_view.controls.append(ft.Text(value=f"[-] TCP is close ! {host}:{port}" , color=ft.colors.RED_300))
                    s.close() 
        #--------------except--------------
        except KeyboardInterrupt:
            page.add(ft.Text(value=f"اطلاعات وارد شده صحیح نمیباشد !\n"))
            page.update()
        except socket.gaierror:
            page.add(ft.Text(value=f"{urlbar.value} موجود نیست"))
            page.update()
        except socket.error:
            page.add(ft.Text(value=f"اتصال انجام نشد"))
            page.update()



    list_view = ft.ListView(expand=True  , padding=13)
    urlbar = ft.TextField(hint_text="آدرس سایت خود را وارد کنید" , expand=False , width=680 , helper_text="example : 192.83.43.2 or google.com" , prefix_text="https://" , suffix_text="/")
    rangebar = ft.TextField(hint_text="رنج پورت را وارد کنید"  , width=320 , helper_text="example : 50 (range  1 to 1000)")
    button_s = ft.ElevatedButton(text="start" , on_click=Port_Scanner , width=100 , height=99)
    #--------------Add To Page--------------
    page.add(
        ft.Row(
            [
                urlbar , rangebar 
            ]
        ) , list_view
        )
    page.add(
        ft.Row(
            [
                button_s
            ] , 
            alignment=ft.MainAxisAlignment.CENTER
            )
        )

ft.app(target=main)