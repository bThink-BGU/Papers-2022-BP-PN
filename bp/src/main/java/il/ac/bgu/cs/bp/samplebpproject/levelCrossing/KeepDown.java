package il.ac.bgu.cs.bp.samplebpproject.levelCrossing;

@SuppressWarnings("serial")
public class KeepDown extends IEvent {
  public static final String NAME = "KeepDown";

  public KeepDown(int i) {
    super(NAME, i);
  }

  public KeepDown() {
    super(NAME);
  }
}
