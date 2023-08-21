package Example1;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Diary {
    private final Map<Integer, DiaryEntry> entries = new HashMap<>();


    public void addEntry(DiaryEntry entry) {
        entries.put(entry.getId(), entry);
    }

    public void getContent() {
        for (DiaryEntry entry : entries.values()) {
            System.out.println(entry.getContent());
        }
    }

    public void updateEntry(int id, String content) {
        DiaryEntry entry = entries.get(id);
        if (entry != null) {
            entry.updateContent(content);
        }
    }

    public List<DiaryEntry> searchEntry() {
        return new ArrayList<>(entries.values());
    }

    public void lockEntry(int id, boolean locked) {
        DiaryEntry entry = entries.get(id);
        if (entry != null) {
            entry.lock(locked);
        }
    }

    public void unlockEntry(int id, boolean locked) {
        DiaryEntry entry = entries.get(id);
        if (entry != null) {
            entry.unlock(locked);
        }
    }

    public void deleteEntry(int id) {
        entries.remove(id);
    }
}
