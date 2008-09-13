#include <glib.h>
#include <gtk/gtk.h>
#include <unistd.h>				// unlink()
#include <stdlib.h>				// getenv()
#include <stdio.h>				// fopen() fdopen() fprintf()
#include <string.h>
#include <fcntl.h>



int main(int argc, char *argv[])
{
		GdkEventClient event =
			{ GDK_CLIENT_EVENT, NULL, TRUE, gdk_atom_intern("_GTK_READ_RCFILES",
				FALSE), 8 };
		gdk_event_send_clientmessage_toall((GdkEvent *) & event);

	return 0;
}
