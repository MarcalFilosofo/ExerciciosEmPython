#! python
def tag_bloco(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == '__main__':
    assert tag_bloco('Incluido com sucesso') == \
        '<div class="success">Incluido com sucesso</div>'
    assert tag_bloco('Impossivel excluir', 'error') == \
        '<div class="error">Impossivel excluir</div>'
    print(tag_bloco('bloco'))