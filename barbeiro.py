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
        elif e.control.text == 'Agendar':
            page.clean()
            tela_agendar()
        elif e.control.icon == ft.icons.PEOPLE:
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

        def voltar(e):
            if e.control.icon == ft.icons.ARROW_BACK_IOS:
                page.clean()
                tela_inicial()
            
            page.update()

        #tesoura_imagem = 'imagesBarbearia/tesoura2.png'

        #TITULO
        cabeca = ft.Column(
            controls=[
                #ver_tesoura,
                ft.Text(
                    value='Barbearia e Salão',
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

        bt_voltar = ft.IconButton(
            icon=ft.icons.ARROW_BACK_IOS,
            icon_color='white',
            on_click=voltar
        )

        bt_voltar = ft.Container(
            content=bt_voltar
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

        page.add(bt_voltar, inicial)

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
            value='Agenda moderna',
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
            style=style,
            on_click=muda_tela
        )

        bt_perfil = ft.TextButton(
            text='Entrar',
            icon=ft.icons.PEOPLE,
            icon_color='white',
            style=ft.ButtonStyle(color={ft.MaterialState.DEFAULT: ft.colors.WHITE}),
            on_click=muda_tela
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

    #TELA AGENDAR
    def tela_agendar():

        page.padding = ft.padding.only(top=15)

        def voltar(e):
            if e.control.icon == ft.icons.ARROW_BACK_IOS:
                page.clean()
                tela_inicial()
            
            page.update()

        bt_voltar = ft.IconButton(
            icon=ft.icons.ARROW_BACK_IOS,
            icon_color='white',
            on_click=voltar
        )

        bt_logar = ft.TextButton(
            icon=ft.icons.PEOPLE,
            icon_color='white',
            on_click=muda_tela
        )

        bt_config = ft.IconButton(
            icon=ft.icons.SETTINGS,
            icon_color='white'
        )
        
        cabeca = ft.Row(
            controls=[
                bt_voltar,
                ft.Row(controls=[ft.Text('Agenda', text_align=ft.TextAlign.CENTER)], alignment=ft.MainAxisAlignment.CENTER, expand=True),
                bt_logar,
                bt_config
            ],
            expand=True
        )

        semanas = ft.ResponsiveRow(
            columns=2,
            controls=[
                ft.Row(
                    col=1,
                    controls=[ft.TextButton('Semana atual', style=ft.ButtonStyle(color={ft.MaterialState.DEFAULT: 'white'}))],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    col=1,
                    controls=[ft.TextButton('Póxima semana', style=ft.ButtonStyle(color={ft.MaterialState.DEFAULT: 'white'}))],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ]
        )


        #ULTIMA ATUALIZAÇÃOOOOOOOOOOO
        organizacao = ft.ResponsiveRow(
            columns=5,
            controls=[
                ft.Container(
                    col=1,
                    content=ft.Column(
                            controls=[
                                ft.TextButton(
                                    'S',
                                    style=ft.ButtonStyle(color={ft.MaterialState.DEFAULT: 'white'})                   
                                )
                            ]
                    ),
                    bgcolor=ft.colors.BLACK12
                )
            ]
        )

        conteudo = ft.Container(
            content=ft.Column(
                controls=[
                    cabeca,
                    ft.Divider(),
                    semanas,
                    ft.Divider(),
                    organizacao
                ],
                spacing=0
            )
        )

        page.add(conteudo)
    
    tela_inicial()

if __name__=="__main__":
    ft.app(main, assets_dir='assets')