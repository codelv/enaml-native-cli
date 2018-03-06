package {{cookiecutter.bundle_id}};

import android.app.Application;

import com.codelv.enamlnative.EnamlApplication;
import com.codelv.enamlnative.EnamlPackage;
import com.codelv.enamlnative.packages.BridgePackage;
import com.codelv.enamlnative.packages.PythonPackage;

import java.util.Arrays;
import java.util.List;

public class MainApplication extends Application implements EnamlApplication {
    @Override
    public List<EnamlPackage> getPackages() {
        return Arrays.<EnamlPackage>asList(
                new BridgePackage(),
                new PythonPackage()
        );
    }

    @Override
    public boolean showDebugMessages() {
        return BuildConfig.DEBUG;
    }
}
