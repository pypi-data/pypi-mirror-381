#include <JuceHeader.h>
#include <pybind11/pybind11.h>

namespace py = pybind11;

class VSTInstrumentHost : private juce::Timer,
                          private juce::MidiInputCallback
{
public:
    VSTInstrumentHost()
    {
        formatManager.addDefaultFormats();
        deviceManager.initialise(0, 2, nullptr, true);
        player.setProcessor(nullptr);
        deviceManager.addAudioCallback(&player);

        auto midiInputs = juce::MidiInput::getAvailableDevices();
        if (!midiInputs.isEmpty())
        {
            auto midiDevice = midiInputs[0];
            deviceManager.setMidiInputDeviceEnabled(midiDevice.identifier, true);
            deviceManager.addMidiInputDeviceCallback(midiDevice.identifier, this);
        }

        startTimerHz(60);
    }

    ~VSTInstrumentHost() override
    {
        auto midiInputs = juce::MidiInput::getAvailableDevices();
        if (!midiInputs.isEmpty())
        {
            auto midiDevice = midiInputs[0];
            deviceManager.removeMidiInputDeviceCallback(midiDevice.identifier, this);
            deviceManager.setMidiInputDeviceEnabled(midiDevice.identifier, false);
        }

        deviceManager.removeAudioCallback(&player);
        player.setProcessor(nullptr);
        plugin.reset();
    }

    void loadPlugin(const std::string& path)
    {
        juce::File pluginFile(path);
        if (!pluginFile.existsAsFile())
            throw std::runtime_error("Plugin file does not exist.");

        juce::PluginDescription desc;
        desc.fileOrIdentifier = path;
        desc.name = pluginFile.getFileName().toStdString();
        desc.pluginFormatName = "VST3";  // adjust as needed

        auto* currentDevice = deviceManager.getCurrentAudioDevice();
        if (currentDevice == nullptr)
            throw std::runtime_error("No audio device available.");

        auto sampleRate = currentDevice->getCurrentSampleRate();
        auto blockSize = currentDevice->getDefaultBufferSize();

        dummyBuffer.setSize(currentDevice->getActiveOutputChannels().countNumberOfSetBits(), (int)blockSize);
        dummyBuffer.clear();

        juce::String errorMessage;
        auto pluginInstance = formatManager.createPluginInstance(desc, sampleRate, blockSize, errorMessage);

        if (!pluginInstance)
            throw std::runtime_error("Failed to load plugin: " + errorMessage.toStdString());

        plugin = std::move(pluginInstance);  // move unique_ptr

        if (!plugin->acceptsMidi())
            throw std::runtime_error("Loaded plugin is not an instrument!");

        plugin->prepareToPlay(sampleRate, blockSize);
        player.setProcessor(plugin.get());
    }

    void showEditor()
    {
        if (!plugin)
            throw std::runtime_error("Plugin not loaded.");

        if (auto* editor = plugin->createEditorIfNeeded())
        {
            window = std::make_unique<juce::DocumentWindow>(
                "Plugin Editor", juce::Colours::black, juce::DocumentWindow::allButtons);

            window->setUsingNativeTitleBar(true);
            window->setContentOwned(editor, true);
            window->setResizable(true, true);
            window->centreWithSize(editor->getWidth(), editor->getHeight());
            window->setVisible(true);
        }
        else
        {
            throw std::runtime_error("Plugin has no editor.");
        }
    }

    std::vector<float> getParameters()
    {
        if (!plugin)
            throw std::runtime_error("Plugin not loaded.");

        std::vector<float> params;
        for (auto* param : plugin->getParameters())
            params.push_back(param->getValue());

        return params;
    }

    void setParameter(int index, float value)
    {
        if (!plugin)
            throw std::runtime_error("Plugin not loaded.");

        auto parameters = plugin->getParameters();
        if (index < 0 || index >= static_cast<int>(parameters.size()))
            throw std::runtime_error("Invalid parameter index.");

        parameters[index]->setValueNotifyingHost(value);
    }

    void sendMidiNoteOn(int note)
    {
        sendMidiMessage(juce::MidiMessage::noteOn(1, note, (juce::uint8)127));
    }

    void sendMidiNoteOff(int note)
    {
        sendMidiMessage(juce::MidiMessage::noteOff(1, note));
    }

    void sendAllNotesOff()
    {
        if (!plugin)
            return;

        juce::MidiBuffer buffer;
        for (int note = 0; note < 128; ++note)
            buffer.addEvent(juce::MidiMessage::noteOff(1, note), 0);

        plugin->processBlock(dummyBuffer, buffer);
    }

private:
    void sendMidiMessage(const juce::MidiMessage& msg)
    {
        if (!plugin)
            return;

        juce::MidiBuffer buffer;
        buffer.addEvent(msg, 0);
        plugin->processBlock(dummyBuffer, buffer);
    }

    void handleIncomingMidiMessage(juce::MidiInput*, const juce::MidiMessage& message) override
    {
        sendMidiMessage(message);
    }

    void timerCallback() override
    {
        if (window)
            window->repaint();
    }

    juce::AudioPluginFormatManager formatManager;
    juce::AudioDeviceManager deviceManager;
    juce::AudioProcessorPlayer player;
    std::unique_ptr<juce::AudioPluginInstance> plugin;
    std::unique_ptr<juce::DocumentWindow> window;
    juce::AudioSampleBuffer dummyBuffer {2, 512};
};

// Expose to Python via PyBind11
PYBIND11_MODULE(vsthost, m)
{
    py::class_<VSTInstrumentHost>(m, "VSTInstrumentHost")
        .def(py::init<>())
        .def("load_plugin", &VSTInstrumentHost::loadPlugin)
        .def("show_editor", &VSTInstrumentHost::showEditor)
        .def("get_parameters", &VSTInstrumentHost::getParameters)
        .def("set_parameter", &VSTInstrumentHost::setParameter)
        .def("send_midi_note_on", &VSTInstrumentHost::sendMidiNoteOn)
        .def("send_midi_note_off", &VSTInstrumentHost::sendMidiNoteOff)
        .def("send_all_notes_off", &VSTInstrumentHost::sendAllNotesOff);
}
