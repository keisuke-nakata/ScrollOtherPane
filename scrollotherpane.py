import sublime, sublime_plugin

class ScrollOtherPaneCommand(sublime_plugin.WindowCommand):
    def run(self, cmd, amount):
        """
        window.run_command("scroll_other_pane", {"command": "scroll_lines", "amount": -12.0})
        """
        ng = self.window.num_groups()
        if ng==1:
            return()
        ag = self.window.active_group()
        target_g = (ag+1) % ng

        target_v = self.window.active_view_in_group(target_g)
        target_v.run_command(cmd, {"amount": amount})
