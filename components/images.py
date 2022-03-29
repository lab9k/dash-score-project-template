from dash import html


def picture(url: str, alt: str, **kwargs) -> html.Img:
    """

    :rtype: html.Img
    :param url: location of the image, can be in the assets folder or an online picture
    :param alt: The alt text of the picture
    :param kwargs: extra keyword arguments will be passed to html.Img
    :return: html.Img
    """
    return html.Img(src=url, alt=alt, **kwargs)


def gallery():
    # TODO: implement gallery mode
    pass
