#! /usr/bin/env python

from pyfeyn.user import *
from math import sin,cos,tan
import pyx 

# paint styles
# https://pyfeyn.hepforge.org/doc/pyfeyn.paint-module.html

model = "TChiHH"
model = "TChiHW"
model = "TChiHZ"


### Defining labels
lspTop_s=r"$\tilde{\chi}^0_1$"
lspBottom_s=r"$\tilde{\chi}^0_1$"
lsp=r"$\tilde{G}$"
dauTop_s = "h"
dauBottom_s = "h"

if model == "TChiHZ":
    dauBottom_s = "Z"

if model == "TChiHW":
    lspTop_s=r"$\tilde{\chi}^0_2$"
    lspBottom_s=r"$\tilde{\chi}^\pm_1$"
    lsp=r"$\tilde{\chi}^0_1$"
    dauBottom_s = r"W$^\pm$"


susycolor = RED
# susycolor = BLACK
linewidth = THICK2

r_blob = 0.4

dx_1 = 1.5
ang_1 = 30./180.*3.1415

dx_h = 1.
ang_h = 40./180.*3.1415
dx_g = 1.7
ang_g = -5./180.*3.1415

processOptions()
fd = FeynDiagram()

in1  = Point(-2.2, -1.5)
in2  = Point(-2.2, 1.5)
blob = Circle(-1,0, radius=r_blob).setFillStyle(GRAY)
P1 = Fermion(in1, blob).addLabel("$p$",displace=-0.2)
P1_label = MultiLine(in1, blob,n=2, dist=0.1)
P2 = Fermion(in2, blob).addLabel("$p$",displace=.17)
P2_label = MultiLine(in2, blob,n=2, dist=0.1)

vtx_top =  Vertex(dx_1,      dx_1*tan(ang_1),  mark=CircleMark())
vtx_toph = Vertex(dx_1+dx_h, dx_1*tan(ang_1)+dx_h*tan(ang_h))
vtx_topg = Vertex(dx_1+dx_g, dx_1*tan(ang_1)+dx_g*tan(ang_g))

vtx_bot =  Vertex(dx_1,      -dx_1*tan(ang_1), mark=CircleMark())
vtx_both = Vertex(dx_1+dx_h, -(dx_1*tan(ang_1)+dx_h*tan(ang_h)))
vtx_botg = Vertex(dx_1+dx_g, -(dx_1*tan(ang_1)+dx_g*tan(ang_g)))


nlsp_top = Vector(blob, vtx_top).setAmplitude(0.1).setFrequency(0.4)
nlsp_topin = Line(blob, vtx_top).addStyle(linewidth).addStyle(susycolor)
# nlsp_top = Gaugino(blob, vtx_top)
# nlsp_top.set3D()
nlsp_top.addLabel(lspTop_s)
nlsp_top.addStyle(linewidth).addStyle(susycolor)
dau_top = Higgs(vtx_top, vtx_toph).addLabel(dauTop_s,displace=0.05, pos = 1.3)
# dau_top = Higgs(vtx_top, vtx_toph).addLabel(dauTop_s,angle=90, pos = 1.3)
dau_top.addStyle(linewidth)
lsp_top = Ghost(vtx_top, vtx_topg).addLabel(lsp,displace=0.005, pos = 1.2)
lsp_top.addStyle(linewidth).addStyle(susycolor)

nlsp_bot = Vector(blob, vtx_bot).setAmplitude(0.1).setFrequency(0.4)
nlsp_botin = Line(blob, vtx_bot).addStyle(linewidth).addStyle(susycolor)
# nlsp_bot = Gaugino(blob, vtx_bot)
# nlsp_bot.set3D()
nlsp_bot.addLabel(lspBottom_s,displace=.34)
nlsp_bot.addStyle(linewidth).addStyle(susycolor)
nlsp_bot.invert()

lsp_bot = Ghost(vtx_bot, vtx_botg).addLabel(lsp,displace=0.01, pos = 1.2)
lsp_bot.addStyle(linewidth).addStyle(susycolor)
if model == "TChiHH": dau_bot = Higgs(vtx_bot, vtx_both).addLabel(dauBottom_s,displace=0., pos = 1.3)
else: dau_bot = Vector(vtx_bot, vtx_both).addLabel(dauBottom_s,displace=0., pos = 1.3).setAmplitude(0.05).setFrequency(0.3)
dau_bot.addStyle(linewidth)

plotname = model+"_diag.pdf"
fd.draw(plotname)

print "\n open "+plotname+"\n"
# os.system ("convert %s_feyn.pdf -transparent white %s_feyn.png" % (name, name))
