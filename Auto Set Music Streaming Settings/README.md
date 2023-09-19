# Auto Set Music Streaming Settings

 This is a tool to automatically configure streaming settings for music tracks in Wwise.
 To use it, double click the executable file with your Wwise project open. It will open a terminal window with prompts and instructions. 
 Compatible with Wwise versions 2021 and 2022.
 
 Here's what it does:
 
 1. First it will ask you for a path to a parent object. If you only want to affect the music tracks inside a specific object, you can pass in a path to it (shift+right click the object and select "Copy path to clipboard" and paste it to the terminal). Alternatively, you can leave this blank to affect all music tracks in the entire project.
 
 2. The tool will automatically enable Stream for all music tracks in scope. Next it will ask you to define values for the other streaming related settings.
 
 3. It will ask you to pass in a value for the Zero Latency and Non-cachable settings. You can type either "true" or "false" for those (or "t" and "f"). It will also catch spelling mistakes and will give you the desired option.
 
 4. It will ask you to pass in a value in milliseconds for the Look-ahead time and the Prefetch length.
 
 5. Any value above can be left blank if you don't want to change it. Simple press enter without typing anything and the script will ignore that setting.
