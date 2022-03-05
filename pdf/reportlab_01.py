from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def mm2p(milimetros):
    return milimetros / 0.352777


def main(args):
    cnv = canvas.Canvas("alomundo.pdf", pagesize=A4)

    posX = mm2p(100)  # valores da posição em mm
    posY = mm2p(150)

    cnv.drawString(posX, posY, "Alô mundo!")
    cnv.save()
    return 0