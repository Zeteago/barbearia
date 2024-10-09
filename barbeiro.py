import flet as ft 

def alerta(texto, cor):
    return ft.AlertDialog(
            title=ft.Text(value=texto, text_align=ft.TextAlign.CENTER),
            open=True,
            bgcolor=cor
        )

def main(page: ft.Page):

    def muda_tela(e):
        if e.control.text == 'Não tenho conta':
            page.clean()
            tela_registro()
        elif e.control.text == 'Já tenho uma conta':
            page.clean()
            tela_login()

        page.update()

    #RESPONSIVIDADE
    if page.window_width < 768:
        page.padding = ft.padding.symmetric(horizontal=20, vertical=20)
        #ver_tesoura = ft.Image(src=tesoura_imagem, width=100, height=100)
        tam_btLogH = 50
        tam_btLogW = 250
    else:
        page.padding = ft.padding.symmetric(horizontal=50, vertical=20)
        #ver_tesoura = ft.Image(src=tesoura_imagem, width=200, height=100)
        tam_btLogH = 50
        tam_btLogW = 250

    style = ft.ButtonStyle(
        shape={
            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(5)
        }
    )

    #TELA DE LOGIN
    def tela_login():

        def login(e):
            if (log_usu.value.strip() == "") or (log_senha.value.strip() == ""):
                page.dialog = alerta('Preencha todos os campos!', 'red')
                page.update()

        #tesoura_imagem = 'imagesBarbearia/tesoura2.png'

        #TITULO
        cabeca = ft.Column(
            controls=[
                #ver_tesoura,
                ft.Text(
                    value='Barbearia',
                    style=ft.TextThemeStyle.HEADLINE_SMALL
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        #BOTOES E INPUTS
        log_usu = ft.TextField(
            label='Usuário',
            border_color='white'
        )

        log_senha = ft.TextField(
            label='Senha',
            border_color='white',
            password=True,
            can_reveal_password=True
        )

        esquece_senha = ft.TextButton(
            text='Esqueci a senha'
        )

        sem_conta = ft.TextButton(
            text='Não tenho conta',
            on_click=muda_tela
        )

        log = ft.Container(
            content=ft.Row(
                controls=[
                    ft.ElevatedButton(
                        text='Entrar',
                        width=tam_btLogW,
                        height=tam_btLogH,
                        bgcolor='white',
                        color='black',
                        style=style,
                        on_click=login
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            padding=ft.padding.only(top=30)
        )

        conteudo = ft.Column(
            controls=[
                log_usu,
                log_senha,
                esquece_senha,
                log,
                sem_conta
            ]
        )

        #JUNÇÃO
        inicial = ft.Column(
            controls=[
                cabeca,
                conteudo
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30,
            expand=True
        )

        page.add(inicial)

    #TELA DE REGISTRO
    def tela_registro():

        def registro(e):

            usuario = usu.value
            senha1 = senha.value
            confirmar_senha = confirm_senha.value

            if (usuario.strip() == "") or (senha1.strip() == "") or (confirmar_senha.strip() == ""):
                page.dialog = alerta('Preencha todos os campos!', 'red')
                page.update()
            elif senha1 != confirmar_senha:
                page.dialog = alerta('As senhas não batem!', 'red')
                page.update()
            else:
                page.dialog = alerta('Registro concluído com exito!', 'green')
                page.clean()
                tela_login()

        #tesoura_imagem = 'imagesBarbearia/tesoura2.png'

        if page.window_width < 768:
            page.padding = ft.padding.symmetric(horizontal=20, vertical=20)
            #ver_tesoura = ft.Image(src=tesoura_imagem, width=100, height=100)
            tam_btLogH = 50
            tam_btLogW = 250
        else:
            page.padding = ft.padding.symmetric(horizontal=50, vertical=20)
            #ver_tesoura = ft.Image(src=tesoura_imagem, width=200, height=100)
            tam_btLogH = 50
            tam_btLogW = 250

        cabeca = ft.Column(
            controls=[
                #ver_tesoura,
                ft.Text(
                    value='Registro',
                    style=ft.TextThemeStyle.HEADLINE_SMALL
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        usu = ft.TextField(
            label='Usuário',
            border_color='white'
        )

        senha = ft.TextField(
            label='Senha',
            border_color='white',
            password=True,
            can_reveal_password=True
        )

        confirm_senha = ft.TextField(
            label='Confirmar senha',
            border_color='white',
            password=True,
            can_reveal_password=True
        )

        sem_conta = ft.TextButton(
            text='Já tenho uma conta',
            on_click=muda_tela
        )

        log = ft.Container(
            content=ft.Row(
                controls=[
                    ft.ElevatedButton(
                        text='Registrar',
                        width=tam_btLogW,
                        height=tam_btLogH,
                        bgcolor='white',
                        color='black',
                        style=style,
                        on_click=registro
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            padding=ft.padding.only(top=30)
        )

        conteudo = ft.Column(
            controls=[
                usu,
                senha,
                confirm_senha,
                log,
                sem_conta
            ]
        )

        regis = ft.Column(
            controls=[
                cabeca,
                conteudo
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30,
            expand=True
        )

        page.add(regis)

    #TELA INICIAL
    def tela_inicial():
        
        titulo = ft.Text(
            value='Barbearia',
            style=ft.TextThemeStyle.HEADLINE_SMALL
        )

        mensagem = ft.Text(
            value='Seja muito bem vindo(a)!'
        )

        bt_agendar = ft.ElevatedButton(
            text='Agendar',
            width=tam_btLogW,
            height=tam_btLogH,
            bgcolor='white',
            color='black',
            style=style
        )

        bt_perfil = ft.IconButton(
            icon=ft.icons.PEOPLE,
            icon_color='white'
        )

        textos = ft.Container(
            content=ft.Column(
                controls=[
                    titulo,
                    mensagem
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=30
            ),
            padding=ft.padding.only(top=100, bottom=100)
        )

        btns = ft.Container(
            content=ft.Column(
                controls=[
                    bt_agendar,
                    bt_perfil
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=100
            )
        )

        conteudo = ft.Container(
            content=ft.Column(
                controls=[
                    textos, 
                    btns
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            expand=True,
            alignment=ft.alignment.center
        )

        page.add(conteudo)

    tela_inicial()

if __name__=="__main__":
    ft.app(main, assets_dir='assets')