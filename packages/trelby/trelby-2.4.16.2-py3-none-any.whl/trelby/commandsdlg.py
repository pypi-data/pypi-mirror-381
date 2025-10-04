import xml.sax.saxutils as xss

import wx
import wx.html

import trelby.util as util


class CommandsDlg(wx.Frame):
    def __init__(self, cfgGl):
        wx.Frame.__init__(
            self, None, -1, _("Commands"), size=(650, 600), style=wx.DEFAULT_FRAME_STYLE
        )

        # self.Center()

        vsizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vsizer)

        s = (
            '<table border="1"><tr><td><b>' + _("Key(s)") + "</b></td>"
            "<td><b>" + _("Command") + "</b></td></tr>"
        )

        for cmd in cfgGl.commands:
            s += '<tr><td bgcolor="#dddddd" valign="top">'

            if cmd.keys:
                for key in cmd.keys:
                    k = util.Key.fromInt(key)
                    s += "%s<br>" % xss.escape(k.toStr())
            else:
                s += _("No key defined") + "<br>"

            s += '</td><td valign="top">'
            s += "%s" % xss.escape(cmd.desc)
            s += "</td></tr>"

        s += "</table>"

        self.html = (
            """
<html><head></head><body>

%s

<pre>
<b>Mouse:</b>

Left click             Position cursor
Left click + drag      Select text
Right click            Unselect

<b>Keyboard shortcuts in Find/Replace dialog:</b>

F                      Find
R                      Replace
</pre>
</body></html>
        """
            % s
        )

        htmlWin = wx.html.HtmlWindow(self)
        rep = htmlWin.GetInternalRepresentation()
        rep.SetIndent(0, wx.html.HTML_INDENT_BOTTOM)
        htmlWin.SetPage(self.html)
        htmlWin.SetFocus()

        vsizer.Add(htmlWin, 1, wx.EXPAND)

        id = wx.NewId()
        menu = wx.Menu()
        menu.Append(id, "&Save as...")

        mb = wx.MenuBar()
        mb.Append(menu, "&File")
        self.SetMenuBar(mb)

        self.Bind(wx.EVT_MENU, self.OnSave, id=id)

        self.Layout()

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseWindow(self, event):
        self.Destroy()

    def OnSave(self, event):
        dlg = wx.FileDialog(
            self,
            _("Filename to save as"),
            wildcard=_("HTML files (*.html)|*.html|All files|*"),
            style=wx.FD_SAVE | wx.OVERWRITE_PROMPT,
        )

        if dlg.ShowModal() == wx.ID_OK:
            util.writeToFile(dlg.GetPath(), self.html, self)

        dlg.Destroy()
