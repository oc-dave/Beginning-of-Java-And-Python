package Example1;

public class DiaryEntry {
    private final int id;
    private String content;
    private boolean locked;

    public DiaryEntry(int id, String content, boolean locked) {
        this.id = id;
        this.content = content;
        this.locked = locked;
    }

    public int getId() {
        return id;
    }

    public void lock(boolean locked) {
        this.locked = locked;
    }

    public void unlock(boolean locked) {
        this.locked = !locked;
    }

    public void updateContent(String newContent) {
        if (!locked) {
            content = newContent;
        } else {
            System.out.println("Diary is locked");
        }
    }

    public String getContent() {
        return content;
    }

    public boolean isLocked() {
        return locked;
    }
}
