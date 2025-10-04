import wx

import trelby.characterreport as characterreport
import trelby.gutil as gutil
import trelby.locationreport as locationreport
import trelby.misc as misc
import trelby.scenereport as scenereport
import trelby.scriptreport as scriptreport
import trelby.util as util


def genSceneReport(mainFrame, sp):
    report = scenereport.SceneReport(sp)

    dlg = misc.CheckBoxDlg(
        mainFrame, _("Report type"), report.inf, _("Information to include:"), False
    )

    ok = False
    if dlg.ShowModal() == wx.ID_OK:
        ok = True

    dlg.Destroy()

    if not ok:
        return

    data = report.generate()

    gutil.showTempPDF(data, sp.cfgGl, mainFrame)


def genLocationReport(mainFrame, sp):
    report = locationreport.LocationReport(scenereport.SceneReport(sp))

    dlg = misc.CheckBoxDlg(
        mainFrame, _("Report type"), report.inf, _("Information to include:"), False
    )

    ok = False
    if dlg.ShowModal() == wx.ID_OK:
        ok = True

    dlg.Destroy()

    if not ok:
        return

    data = report.generate()

    gutil.showTempPDF(data, sp.cfgGl, mainFrame)


def genCharacterReport(mainFrame, sp):
    report = characterreport.CharacterReport(sp)

    if not report.cinfo:
        wx.MessageBox(_("No characters speaking found."), _("Error"), wx.OK, mainFrame)

        return

    charNames = []
    for s in util.listify(report.cinfo, "name"):
        charNames.append(misc.CheckBoxItem(s))

    dlg = misc.CheckBoxDlg(
        mainFrame,
        _("Report type"),
        report.inf,
        _("Information to include:"),
        False,
        charNames,
        _("Characters to include:"),
        True,
    )

    ok = False
    if dlg.ShowModal() == wx.ID_OK:
        ok = True

        for i in range(len(report.cinfo)):
            report.cinfo[i].include = charNames[i].selected

    dlg.Destroy()

    if not ok:
        return

    data = report.generate()

    gutil.showTempPDF(data, sp.cfgGl, mainFrame)


def genScriptReport(mainFrame, sp):
    report = scriptreport.ScriptReport(sp)
    data = report.generate()

    gutil.showTempPDF(data, sp.cfgGl, mainFrame)
