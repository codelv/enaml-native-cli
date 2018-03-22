package {{cookiecutter.bundle_id}};

import com.codelv.enamlnative.EnamlActivity;
import com.codelv.enamlnative.EnamlPackage;
import com.codelv.enamlnative.Bridge;

public class {{cookiecutter.widget_name}}Package implements EnamlPackage {

    EnamlActivity mActivity;

    @Override
    public void onCreate(EnamlActivity activity) {
        mActivity = activity;
    }

    /**
     * Add special bridge packers required by your components
     */
    @Override
    public void onStart() {
        Bridge bridge = mActivity.getBridge();
    }

    @Override
    public void onResume() {

    }

    @Override
    public void onPause() {

    }

    @Override
    public void onStop() {

    }

    @Override
    public void onDestroy() {

    }
}
