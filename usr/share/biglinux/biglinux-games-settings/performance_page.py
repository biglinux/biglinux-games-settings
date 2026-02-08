from base_page import BaseSettingsPage, _

class PerformancePage(BaseSettingsPage):
    def __init__(self, main_window, **kwargs):
        super().__init__(main_window, **kwargs)

        # Create the container (base method)
        content = self.create_scrolled_content()

        ## GROUP ##

        # Performance
        group = self.create_group(
            _("Performance"),
            _("BigLinux performance tweaks."),
            "performance"
        )
        content.append(group)

        # Disable Visual Effects
        self.create_row(
            group,
            _("Disable Visual Effects"),
            _("Disables KWin visual effects (blur, shadows, animations). Reduces GPU load and frees memory."),
            "disableVisualEffects",
            "disable-visual-effects-symbolic"
        )
        # CPU Maximum Performance
        self.create_row(
            group,
            _("CPU Maximum Performance"),
            _("Forces maximum processor performance mode. Ensures the processor uses maximum frequency."),
            "cpuMaximumPerformance",
            "cpu-maximum-performance-symbolic"
        )
        # Disable Baloo Indexer
        self.create_row(
            group,
            _("Disable Baloo Indexer"),
            _("Disables the Baloo file indexer. Avoids disk I/O overhead."),
            "disableBalooIndexer",
            "disable-baloo-indexer-symbolic"
        )
        # Unload S.M.A.R.T Monitor
        self.create_row(
            group,
            _("Unload S.M.A.R.T Monitor"),
            _("Disables S.M.A.R.T disk monitoring. Reduces disk I/O and CPU usage."),
            "unloadSmartMonitor",
            "unload-smart-monitor-symbolic"
        )
        # Meltdown mitigations
        link_meltdown = "https://meltdownattack.com"
        self.create_row(
            group,
            _("Meltdown Mitigations off"),
            _("Using mitigations=off will make your machine faster and less secure! For more information see: <a href='{l}'>{l}</a>").format(l=link_meltdown),
            "meltdownMitigations",
            "meltdown-mitigations-symbolic"
        )
        # noWatchdog
        self.create_row(
            group,
            _("noWatchdog"),
            _("Disables the hardware watchdog and TSC clocksource systems, maintaining high performance but removing automatic protections against system crashes."),
            "noWatchdog",
            "watchdog-symbolic"
        )

        self.sync_all_switches()
